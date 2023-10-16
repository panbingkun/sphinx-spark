#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
pandas-on-Spark specific features.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyspark.pandas.frame import DataFrame

class PandasOnSparkFrameMethods:
    """pandas-on-Spark specific features for DataFrame."""

    def __init__(self, frame: "DataFrame"):
        self._psdf = frame

    def apply_batch(self, frame: "DataFrame") -> "DataFrame":
        """
        Apply a function that takes pandas DataFrame and outputs pandas DataFrame. The pandas
        DataFrame given to the function is of a batch used internally.

        See also `Transform and apply a function
        <https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/transform_apply.html>`_.

        Parameters
        ----------
        func : function
            Function to apply to each pandas frame.
        args : tuple
            Positional arguments to pass to `func` in addition to the
            array/series.
        **kwds
            Additional keyword arguments to pass as keywords arguments to
            `func`.

        Returns
        -------
        DataFrame

        See Also
        --------
        DataFrame.apply: For row/columnwise operations.
        DataFrame.applymap: For elementwise operations.
        DataFrame.aggregate: Only perform aggregating type operations.
        DataFrame.transform: Only perform transforming type operations.
        Series.pandas_on_spark.transform_batch: transform the search as each pandas chunks.

        Examples
        --------
        >>> df = ps.DataFrame([(1, 2), (3, 4), (5, 6)], columns=['A', 'B'])
        >>> df
           A  B
        0  1  2
        1  3  4
        2  5  6
        """
        return frame