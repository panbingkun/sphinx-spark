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

from typing import (
    Any,
    Generic,
)

from pandas.core.accessor import CachedAccessor

from pyspark.pandas._typing import (
    T,
)
from pyspark.pandas.accessors import PandasOnSparkFrameMethods
from pyspark.pandas.generic import Frame

class DataFrame(Frame, Generic[T]):

    def __init__(  # type: ignore[no-untyped-def]
        self, data=None, index=None, columns=None, dtype=None, copy=False
    ):
        index_assigned = False

    def add(self, other: Any) -> "DataFrame":
        return self + other

    # create accessor for pandas-on-Spark specific methods.
    pandas_on_spark = CachedAccessor("pandas_on_spark", PandasOnSparkFrameMethods)
