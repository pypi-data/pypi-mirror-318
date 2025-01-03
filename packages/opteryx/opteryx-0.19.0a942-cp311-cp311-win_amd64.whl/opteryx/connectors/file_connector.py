# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# See the License at http://www.apache.org/licenses/LICENSE-2.0
# Distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.

"""
The file connector provides the reader for when a file name is provided as the
dataset name in a query.
"""

import os
from typing import Dict
from typing import Optional

import pyarrow
from orso.schema import RelationSchema
from orso.types import OrsoTypes

from opteryx.connectors.base.base_connector import BaseConnector
from opteryx.connectors.capabilities import PredicatePushable
from opteryx.exceptions import DataError
from opteryx.exceptions import DatasetNotFoundError
from opteryx.utils.file_decoders import get_decoder

# Define os.O_BINARY for non-Windows platforms if it's not already defined
if not hasattr(os, "O_BINARY"):
    os.O_BINARY = 0  # Value has no effect on non-Windows platforms


class FileConnector(BaseConnector, PredicatePushable):
    __mode__ = "Blob"
    __type__ = "FILE"
    _byte_array: Optional[bytes] = None  # Instance attribute to store file bytes

    PUSHABLE_OPS: Dict[str, bool] = {
        "Eq": True,
        "NotEq": True,
        "Gt": True,
        "GtEq": True,
        "Lt": True,
        "LtEq": True,
    }

    PUSHABLE_TYPES = {
        OrsoTypes.BLOB,
        OrsoTypes.BOOLEAN,
        OrsoTypes.DOUBLE,
        OrsoTypes.INTEGER,
        OrsoTypes.VARCHAR,
        OrsoTypes.TIMESTAMP,
        OrsoTypes.DATE,
    }

    @property
    def interal_only(self):
        return True

    def __init__(self, *args, **kwargs):
        BaseConnector.__init__(self, **kwargs)
        PredicatePushable.__init__(self, **kwargs)
        if ".." in self.dataset or self.dataset[0] in ("\\", "/", "~"):
            # Don't find any datasets which look like path traversal
            raise DatasetNotFoundError(dataset=self.dataset)
        self.decoder = get_decoder(self.dataset)

    def _read_file(self) -> None:
        """
        Reads the dataset file and stores its content in _byte_array attribute.
        """
        if self._byte_array is None:
            file_descriptor = os.open(self.dataset, os.O_RDONLY | os.O_BINARY)
            try:
                self._byte_array = os.read(file_descriptor, os.path.getsize(self.dataset))
            finally:
                os.close(file_descriptor)

    def read_dataset(
        self, columns: list = None, predicates: list = None, **kwargs
    ) -> pyarrow.Table:
        """
        Reads the dataset file and decodes it.

        Returns:
            An iterator containing a single decoded pyarrow.Table.
        """
        self._read_file()

        try:
            num_rows, num_columns, decoded = self.decoder(
                self._byte_array, projection=columns, selection=predicates
            )
        except Exception as err:
            raise DataError(f"Unable to read file ({err})") from err

        self.statistics.rows_seen += num_rows
        yield decoded

    def get_dataset_schema(self) -> RelationSchema:
        """
        Retrieves the schema from the dataset file.

        Returns:
            The schema of the dataset.
        """
        if self.schema is not None:
            return self.schema

        self._read_file()
        self.schema = self.decoder(self._byte_array, just_schema=True)
        return self.schema
