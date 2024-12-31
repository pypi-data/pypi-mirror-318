# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# See the License at http://www.apache.org/licenses/LICENSE-2.0
# Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.

"""
These are a set of functions that can be applied to data.
"""

import datetime
import decimal
import time

import numpy
import orjson
import pyarrow
from orso.cityhash import CityHash64
from pyarrow import ArrowNotImplementedError
from pyarrow import compute

import opteryx
from opteryx.compiled.list_ops import array_encode_utf8 as to_blob
from opteryx.compiled.list_ops import list_contains_any
from opteryx.exceptions import FunctionNotFoundError
from opteryx.exceptions import IncorrectTypeError
from opteryx.functions import date_functions
from opteryx.functions import number_functions
from opteryx.functions import other_functions
from opteryx.functions import string_functions
from opteryx.utils import dates


def array_encode_utf8(arr):
    try:
        # array_encode_utf8 is fast but brittle
        return to_blob(arr)
    except:
        return [None if s is None else str(s).encode() for s in arr]


def _get(array, key):
    # Determine the type of the first element (assuming homogeneous array)
    first_element = next((item for item in array if item is not None), None)
    if first_element is None:
        return numpy.full(len(array), None)

    key = key[0]
    if isinstance(first_element, dict):
        # Handle dict type
        from opteryx.compiled.list_ops import cython_arrow_op

        return cython_arrow_op(array, key)
    if isinstance(key, str):
        import simdjson

        def extract(doc, elem):
            value = simdjson.Parser().parse(doc).get(elem)  # type:ignore
            if hasattr(value, "as_list"):
                return value.as_list()
            if hasattr(value, "as_dict"):
                return value.as_dict()
            return value

        try:
            return pyarrow.array([None if d is None else extract(d, key) for d in array])
        except ValueError:
            raise IncorrectTypeError(
                "VARCHAR subscripts can only be used on STRUCT or columns with valid JSON documents."
            )
    try:
        index = int(key)
    except Exception:
        raise IncorrectTypeError("VARCHAR and ARRAY values must be subscripted with NUMERIC values")
    if isinstance(first_element, numpy.ndarray):
        # NumPy-specific optimization
        from opteryx.compiled.list_ops import cython_get_element_op

        return cython_get_element_op(array, key)

    if isinstance(first_element, (list, str, pyarrow.ListScalar)):
        # Handle list type
        return [item[index] if item is not None and len(item) > index else None for item in array]

    raise IncorrectTypeError(f"Cannot subscript {type(first_element).__name__} values")


def _get_string(array, key):
    key = key[0]
    return pyarrow.array(
        [None if i != i else str(i) for i in (item.get(key) for item in array)],
        type=pyarrow.string(),
    )


def cast_varchar(arr):
    if len(arr) > 0 and all(i is None or isinstance(i, dict) for i in arr[:100]):
        return [orjson.dumps(n).decode() if n is not None else None for n in arr]
    return compute.cast(arr, "string")


def cast_blob(arr):
    """
    Checks if the first 100 elements of arr are either None or bytes.
    If true, returns the original array. Otherwise, converts all elements
    to strings and then encodes them to bytes.

    Parameters:
    arr (list): The input list to be checked and potentially converted.

    Returns:
    list: The original list if all elements in the first 100 are None or bytes,
          otherwise a new list with all elements converted to bytes.
    """
    if len(arr) > 0 and all(i is None or isinstance(i, bytes) for i in arr[:100]):
        return arr
    return [None if a is None else str(a).encode() for a in arr]


def fixed_value_function(function, context):
    from orso.types import OrsoTypes

    if function not in {
        "CONNECTION_ID",
        "CURRENT_DATE",
        "CURRENT_TIME",
        "DATABASE",
        "E",
        "NOW",
        "PHI",
        "PI",
        "TODAY",
        "USER",
        "UTC_TIMESTAMP",
        "VERSION",
        "YESTERDAY",
    }:
        return None, None

    if function in ("VERSION",):
        return OrsoTypes.VARCHAR, opteryx.__version__
    if function in ("NOW", "CURRENT_TIME", "UTC_TIMESTAMP"):
        return OrsoTypes.TIMESTAMP, numpy.datetime64(context.connection.connected_at)
    if function in ("CURRENT_DATE", "TODAY"):
        return OrsoTypes.DATE, numpy.datetime64(context.connection.connected_at.date())
    if function in ("YESTERDAY",):
        return OrsoTypes.DATE, numpy.datetime64(
            context.connection.connected_at.date() - datetime.timedelta(days=1), "D"
        )
    if function == "CONNECTION_ID":
        return OrsoTypes.INTEGER, context.connection.connection_id
    if function == "DATABASE":
        return OrsoTypes.VARCHAR, context.connection.schema or "DEFAULT"
    if function == "USER":
        return OrsoTypes.VARCHAR, context.connection.user or "ANONYMOUS"
    if function == "PI":
        return OrsoTypes.DOUBLE, 3.14159265358979323846264338327950288419716939937510
    if function == "PHI":
        # the golden ratio
        return OrsoTypes.DOUBLE, 1.61803398874989484820458683436563811772030917980576
    if function == "E":
        # eulers number
        return OrsoTypes.DOUBLE, 2.71828182845904523536028747135266249775724709369995
    return None, None


def safe(func, *parms):
    """execute a function, return None if fails"""
    try:
        return func(*parms)
    except (
        ValueError,
        IndexError,
        TypeError,
        ArrowNotImplementedError,
        AttributeError,
        decimal.InvalidOperation,
    ):
        return None


def try_cast(_type):
    """cast a column to a specified type"""

    bools = {
        "TRUE": True,
        "FALSE": False,
        "ON": True,
        "OFF": False,
        "YES": True,
        "NO": False,
        "1": True,
        "0": False,
        "1.0": True,
        "0.0": False,
    }

    casters = {
        "BOOLEAN": lambda x: bools.get(str(x).upper()),
        "DOUBLE": float,
        "BLOB": lambda x: str(x).encode() if x is not None and not isinstance(x, bytes) else x,
        "INTEGER": lambda x: int(float(x)),
        "DECIMAL": decimal.Decimal,
        "VARCHAR": lambda x: str(x) if x is not None else x,
        "TIMESTAMP": dates.parse_iso,
        "STRUCT": orjson.loads,
        "DATE": lambda x: dates.parse_iso(x).date(),
    }
    if _type in casters:

        def _inner(arr):
            caster = casters[_type]
            return [safe(caster, i) for i in arr]

        return _inner
    raise FunctionNotFoundError(message=f"Internal function to cast values to `{_type}` not found.")


def _iterate_single_parameter(func):
    def _inner(array):
        return numpy.array(list(map(func, array)))

    return _inner


def _sort(func):
    def _inner(array):
        return pyarrow.array([func(item) for item in array])

    return _inner


def _iterate_double_parameter(func):
    """
    for functions called FUNCTION(field, literal)
    """

    def _inner(array, literal):
        if isinstance(array, str):
            array = [array]
        return [func(item, literal[index]) for index, item in enumerate(array)]

    return _inner


def _iterate_double_parameter_field_second(func):
    """
    for functions called FUNCTION(LITERAL, FIELD)
    """

    def _inner(literal, array):
        if isinstance(array, str):
            array = [array]
        return [func(literal, item) for item in array]

    return _inner


def get_len(obj):
    """len, but nullsafe"""
    if hasattr(obj, "__len__"):
        return len(obj)
    return None


def _coalesce(*arrays):
    """
    Element-wise coalesce function for multiple numpy arrays.
    Selects the first non-None item in each row across the input arrays.

    Parameters:
        arrays: tuple of numpy arrays

    Returns:
        numpy array with coalesced values
    """
    # Start with an array full of None values
    result = numpy.array(arrays[0], dtype=object)

    mask = result == None

    for arr in arrays[1:]:
        mask = numpy.array([None if value != value else value for value in result]) == None
        numpy.copyto(result, arr, where=mask)

    return result


def select_values(boolean_arrays, value_arrays):
    """
    Build a result array based on boolean conditions and corresponding value arrays.

    Parameters:
    - boolean_arrays: List[np.ndarray], list of boolean arrays representing conditions.
    - value_arrays: List[np.ndarray], list of arrays with values corresponding to each condition.

    Returns:
    - np.ndarray: Result array with selected values or False where no condition is met.
    """
    # Ensure the input lists are not empty and have the same length
    if not boolean_arrays or not value_arrays or len(boolean_arrays) != len(value_arrays):
        raise ValueError("Input lists must be non-empty and of the same length.")

    # Initialize the result array with False, assuming no condition will be met
    result = numpy.full(len(boolean_arrays[0]), None)

    # Iterate over pairs of boolean and value arrays
    for condition, values in zip(reversed(boolean_arrays), reversed(value_arrays)):
        # Update the result array where the condition is True
        numpy.putmask(result, condition, values)

    return result


def sleep(x):
    time.sleep(x[0] / 1000)  # Sleep for x[0] milliseconds
    return x[0]


DEPRECATED_FUNCTIONS = {
    "LIST": "ARRAY_AGG",  # deprecated, remove 0.19.0
    "MAXIMUM": "MAX",  # deprecated, remove 0.19.0
    "MINIMUM": "MIN",  # deprecated, remove 0.19.0
    "AVERAGE": "AVG",  # deprecated, remove 0.19.0
    "NUMERIC": "DOUBLE",  # deprecated, remove 0.19.0
    "CEILING": "CEIL",  # deprecated, remove 0.19.0
    "ABSOLUTE": "ABS",  # deprecated, remove 0.19.0
    "TRUNCATE": "TRUNC",  # deprecated, remove 0.19.0
    "LIST_CONTAINS_ANY": "ARRAY_CONTAINS_ANY",  # deprecated, remove 0.20.0
    "LIST_CONTAINS_ALL": "ARRAY_CONTAINS_ALL",  # deprecated, remove 0.20.0
    "STRUCT": None,  # deprecated, remove 0.21.0
}

# fmt:off
# Function definitions optionally include the type and the function.
# The type is needed particularly when returning Python objects that
# the first entry is NONE.
FUNCTIONS = {
    "VERSION": lambda x: None, # *
    "CONNECTION_ID": lambda x: None, # *
    "DATABASE": lambda x: None, # *
    "USER": lambda x: None, # *
    # DEBUG: "SLEEP": lambda x: [sleep(x)], # SLEEP is only available in 'debug' mode

    # TYPE CONVERSION
    "TIMESTAMP": lambda x: compute.cast(x, pyarrow.timestamp("us")),
    "BOOLEAN": lambda x: compute.cast(x, "bool"),
    "NUMERIC": lambda x: compute.cast(x, "float64"),
    "INTEGER": lambda x: compute.cast(x, "int64", safe=False),
    "DOUBLE": lambda x: compute.cast(x, "float64"),
    "FLOAT": lambda x: compute.cast(x, "float64"),
    "DECIMAL": lambda x: compute.cast(x, pyarrow.decimal128(19)),
    "VARCHAR": cast_varchar,
    "STRING": cast_varchar,
    "STR": cast_varchar,
    "STRUCT": _iterate_single_parameter(lambda x: orjson.loads(str(x)) if x is not None else None),
    "DATE":  lambda x: compute.cast(x, pyarrow.date32()),
    "BLOB": cast_blob,
    "TRY_TIMESTAMP": try_cast("TIMESTAMP"),
    "TRY_BOOLEAN": try_cast("BOOLEAN"),
    "TRY_NUMERIC": try_cast("DOUBLE"),
    "TRY_VARCHAR": try_cast("VARCHAR"),
    "TRY_BLOB": try_cast("BLOB"),
    "TRY_STRING": try_cast("VARCHAR"),  # alias for VARCHAR
    "TRY_STRUCT": try_cast("STRUCT"),
    "TRY_INTEGER": try_cast("INTEGER"),
    "TRY_DECIMAL": try_cast("DECIMAL"),
    "TRY_DOUBLE": try_cast("DOUBLE"),
    "TRY_DATE": try_cast("DATE"),

    # CHARS
    "CHAR": string_functions.to_char,
    "ASCII": string_functions.to_ascii,

    # STRINGS
    "LEN": _iterate_single_parameter(get_len),  # LENGTH(str) -> int
    "LENGTH": _iterate_single_parameter(get_len),  # LENGTH(str) -> int
    "UPPER": compute.utf8_upper,  # UPPER(str) -> str
    "LOWER": compute.utf8_lower,  # LOWER(str) -> str
    "LEFT": string_functions.string_slicer_left,
    "RIGHT": string_functions.string_slicer_right,
    "REVERSE": compute.utf8_reverse,
    "SOUNDEX": string_functions.soundex,
    "TITLE": compute.utf8_title,
    "CONCAT": string_functions.concat,
    "CONCAT_WS": string_functions.concat_ws,
    "STARTS_WITH": string_functions.starts_w,
    "ENDS_WITH": string_functions.ends_w,
    "SUBSTRING": string_functions.substring,
    "POSITION": _iterate_double_parameter(string_functions.position),
    "TRIM": string_functions.trim,
    "LTRIM": string_functions.ltrim,
    "RTRIM": string_functions.rtrim,
    "LPAD": string_functions.left_pad,
    "RPAD": string_functions.right_pad,
    "LEVENSHTEIN": string_functions.levenshtein,
    "SPLIT": string_functions.split,
    "MATCH_AGAINST": string_functions.match_against,
    "REGEXP_REPLACE": string_functions.regex_replace,

    # HASHING & ENCODING
    "HASH": _iterate_single_parameter(lambda x: hex(CityHash64(str(x)))[2:]),
    "MD5": _iterate_single_parameter(string_functions.get_md5),
    "SHA1": _iterate_single_parameter(string_functions.get_sha1),
    "SHA224": _iterate_single_parameter(string_functions.get_sha224),
    "SHA256": _iterate_single_parameter(string_functions.get_sha256),
    "SHA384": _iterate_single_parameter(string_functions.get_sha384),
    "SHA512": _iterate_single_parameter(string_functions.get_sha512),
    "RANDOM": number_functions.random_number,
    "RAND": number_functions.random_number,
    "NORMAL": number_functions.random_normal,
    "RANDOM_STRING": number_functions.random_string,
    "BASE64_ENCODE": _iterate_single_parameter(string_functions.get_base64_encode),
    "BASE64_DECODE": _iterate_single_parameter(string_functions.get_base64_decode),
    "BASE85_ENCODE": _iterate_single_parameter(string_functions.get_base85_encode),
    "BASE85_DECODE": _iterate_single_parameter(string_functions.get_base85_decode),
    "HEX_ENCODE": _iterate_single_parameter(string_functions.get_hex_encode),
    "HEX_DECODE": _iterate_single_parameter(string_functions.get_hex_decode),

    # OTHER
    "GET": _get,
    "GET_STRING": _get_string,
    "LIST_CONTAINS": _iterate_double_parameter(other_functions.list_contains),
    "ARRAY_CONTAINS": _iterate_double_parameter(other_functions.list_contains),
    "LIST_CONTAINS_ANY": list_contains_any, 
    "ARRAY_CONTAINS_ANY": list_contains_any, 
    "LIST_CONTAINS_ALL": other_functions.list_contains_all,
    "ARRAY_CONTAINS_ALL": other_functions.list_contains_all,
    "SEARCH": other_functions.search,
    "COALESCE": _coalesce,
    "IFNULL": other_functions.if_null,
    "IFNOTNULL": other_functions.if_not_null,
    "SORT": _sort(numpy.sort),
    "GREATEST": _iterate_single_parameter(numpy.nanmax),
    "LEAST": _iterate_single_parameter(numpy.nanmin),
    "IIF": numpy.where,
#    "GENERATE_SERIES": series.generate_series,
    "NULLIF": other_functions.null_if,
    "CASE": select_values, #other_functions.case_when,
    "JSONB_OBJECT_KEYS": other_functions.jsonb_object_keys,

    # Vector
    "COSINE_SIMILARITY": other_functions.cosine_similarity,

    # NUMERIC
    "ROUND": number_functions.round,
    "FLOOR": number_functions.floor,
    "CEIL": number_functions.ceiling,
    "CEILING": number_functions.ceiling, # deprecated, remove 0.19.0
    "ABS": compute.abs,
    "ABSOLUTE": compute.abs, # deprecated, remove 0.19.0
    "SIGN": compute.sign,
    "SIGNUM": compute.sign,
    "SQRT": compute.sqrt,
    "TRUNC": compute.trunc,
    "TRUNCATE": compute.trunc,  # deprecated, remove 0.19.0
    "PI": lambda x: None, # *
    "PHI": lambda x: None, # *
    "E": lambda x: None, # *
    "INT": _iterate_single_parameter(int),
    "POWER": number_functions.safe_power,
    "LN": compute.ln,
    "LOG10": compute.log10,
    "LOG2": compute.log2,
    "LOG": compute.logb,

    # DATES & TIMES
    "DATE_TRUNC": _iterate_double_parameter_field_second(dates.date_trunc),
    "TIME_BUCKET": date_functions.date_floor,
    "DATEDIFF": date_functions.date_diff,
    "TIMEDIFF": date_functions.time_diff,
    "DATEPART": date_functions.date_part,
    "DATE_FORMAT": date_functions.date_format,
    "CURRENT_TIME": lambda x: None, # *
    "UTC_TIMESTAMP": lambda x: None, # *
    "NOW": lambda x: None, # *
    "CURRENT_DATE": lambda x: None, # *
    "TODAY": lambda x: None, # *
#    "TIME": _repeat_no_parameters(date_functions.get_time),
    "YESTERDAY": lambda x: None, # *
#    "DATE": lambda x: compute.cast(x, "date32"), #_iterate_single_parameter(date_functions.get_date),
    "YEAR": compute.year,
    "MONTH": compute.month,
    "DAY": compute.day,
    "WEEK": compute.iso_week,
    "HOUR": compute.hour,
    "MINUTE": compute.minute,
    "SECOND": compute.second,
    "QUARTER": compute.quarter,
    "FROM_UNIXTIME": date_functions.from_unixtimestamp,
    "UNIXTIME": date_functions.unixtime,

}
# fmt:on


def apply_function(function: str = None, *parameters):
    compressed = False

    if not isinstance(parameters[0], int) and function not in (
        "IFNULL",
        "LIST_CONTAINS_ANY",
        "LIST_CONTAINS_ALL",
        "ARRAY_CONTAINS_ANY",
        "ARRAY_CONTAINS_ALL",
        "CONCAT",
        "CONCAT_WS",
        "IIF",
        "COALESCE",
        "SUBSTRING",
        "CASE",
    ):
        morsel_size = len(parameters[0])
        null_positions = numpy.zeros(morsel_size, dtype=numpy.bool_)

        for parameter in parameters:
            # compute null positions
            null_positions = numpy.logical_or(
                null_positions,
                compute.is_null(parameter, nan_is_null=True),
            )

        # Early exit if all values are null
        if null_positions.all():
            return numpy.array([None] * morsel_size)

        if null_positions.any() and all(isinstance(arr, numpy.ndarray) for arr in parameters):
            # if we have nulls and the value array is a numpy arrays, we can speed things
            # up by removing the nulls from the calculations, we add the rows back in
            # later
            valid_positions = ~null_positions
            parameters = [arr.compress(valid_positions) for arr in parameters]
            compressed = True

    interim_results = FUNCTIONS[function](*parameters)

    if compressed:
        # fill the result set
        results = numpy.array([None] * morsel_size, dtype=object)
        numpy.place(results, valid_positions, interim_results)
        return results

    return interim_results


def is_function(name):
    """
    sugar
    """
    return name.upper() in FUNCTIONS


def functions():
    return list(FUNCTIONS.keys())
