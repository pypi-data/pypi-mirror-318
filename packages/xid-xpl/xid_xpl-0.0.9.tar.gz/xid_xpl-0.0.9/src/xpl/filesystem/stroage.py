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
from .entry import Entry


#--------------------------------------------------------------------------------
# 전역 상수 목록.
#--------------------------------------------------------------------------------
EMPTY: str = ""



#--------------------------------------------------------------------------------
# 스토리지 항목.
#--------------------------------------------------------------------------------
TEntry = TypeVar("TEntry", bound = "Entry")
class Storage(Entry[TEntry]):
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self, name: str, **keywordArguments) -> None:
		base = super()
		base.__init__(name, **keywordArguments)

		# 마운트 된 스토리지 위에 또 다른 마운트 된 부모 스토리지가 존재할 수 있는가?
		# base.Parent = None