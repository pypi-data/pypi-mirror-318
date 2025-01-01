#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Generic, Iterable, Iterator, Optional, Sequence, Type, TypeVar, Tuple, Union
from typing import ItemsView, KeysView, ValuesView
from typing import Any, List, Dict, Set
from typing import cast, overload
import builtins
from enum import Enum, auto
from xpl import Builtins
from xpl import PlatformType, Environment
from .basescriptmanager import BaseScriptManager
# Environment.GetPlatformType()


#--------------------------------------------------------------------------------
# 배치 스크립트 매니저.
# - 윈도우 스크립팅.
#--------------------------------------------------------------------------------
class BatchScriptManager(BaseScriptManager):
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	__textlines: list


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		base = super()
		base.__init__()

		self.__textlines: list = list()