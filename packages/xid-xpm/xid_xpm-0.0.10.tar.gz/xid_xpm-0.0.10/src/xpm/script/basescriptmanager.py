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
# Environment.GetPlatformType()


class ScriptType(Enum):
	BATCH = auto()
	SHELL = auto()



#--------------------------------------------------------------------------------
# 스크립트 기능 종류.
#--------------------------------------------------------------------------------
class ScriptFunctionType(Enum):
	NONE = auto() # required.

	# 가상 환경.
	VENV_CREATE = auto() # required.
	VENV_DESTROY = auto() # required.
	VENV_ENABLE = auto() # required.
	VENV_DISABLE = auto() # required.
	VENV_UPDATE = auto() # required.
	VENV_UPDATE_FORCE = auto()

	# 실행.
	EXECUTE_SOURCE = auto() # required.
	EXECUTE_TEST = auto()

	# 빌드.
	BUILD_EXECUTABLE = auto() # required.
	BUILD_ARCHIVE = auto() # required.
	BUILD_MSI = auto()


	# 서비스.
	# Windows (service / nssm)
	# Linux (servicectl)
	# MacOS (brew / launchctl)
	SERVICE_REGISTER = auto()
	SERVICE_UNREGISTER = auto()
	SERVICE_START = auto()
	SERVICE_STOP = auto()
	SERVICE_RESTART = auto()
	SERVICE_STATUS = auto()
	SERVICE_UPDATE_DEPLOY = auto()

	# 로그.
	JOURNAL = auto()

	# 웹서버.
	NGINX_SERVICE_RELOAD = auto()
	NGINX_SERVICE_TEST = auto()




#--------------------------------------------------------------------------------
# 스크립트 매니저.
# - os 별로 현재 프로젝트에 맞는 스크립트를 생성.
#--------------------------------------------------------------------------------
class BaseScriptManager:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	__textlines: list


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		self.__textlines: list = list()


	#--------------------------------------------------------------------------------
	# 실행.
	#--------------------------------------------------------------------------------
	def Clear(self) -> None:
		self.__textlines.clear()


	#--------------------------------------------------------------------------------
	# 실행.
	#--------------------------------------------------------------------------------
	def AddFunction(self, type: ScriptFunctionType) -> None:
		self.__textlines.clear()