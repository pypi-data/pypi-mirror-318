#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Generic, Iterable, Iterator, Optional, Sequence, Type, TypeVar, Tuple, Union
from typing import ItemsView, KeysView, ValuesView
from typing import Any, List, Dict, Set
from typing import cast, overload
import os
from ..core import Builtins
from .stroage import Storage


#--------------------------------------------------------------------------------
# 전역 상수 목록.
#--------------------------------------------------------------------------------
EMPTY: str = ""



#--------------------------------------------------------------------------------
# 드라이브 항목.
#--------------------------------------------------------------------------------
TEntry = TypeVar("TEntry", bound = "Entry")
class Drive(Storage[TEntry]):
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------

	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self, name: str, **keywordArguments) -> None:
		base = super()
		base.__init__(name, **keywordArguments)