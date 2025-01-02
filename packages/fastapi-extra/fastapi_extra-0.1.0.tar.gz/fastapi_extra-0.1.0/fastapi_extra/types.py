__author__ = "ziyan.yin"
__date__ = "2024-12-25"


import datetime
import decimal
from typing import Any, TypeVar, Union

Comparable = Union[int, float, decimal.Decimal, datetime.datetime, datetime.date, datetime.time]
Serializable = Union[Comparable, bool, str, None]


T = TypeVar("T", bound=Any)
E = TypeVar("E", bound=Exception)
C = TypeVar("C", bound=Comparable)
S = TypeVar("S", bound=Serializable)
