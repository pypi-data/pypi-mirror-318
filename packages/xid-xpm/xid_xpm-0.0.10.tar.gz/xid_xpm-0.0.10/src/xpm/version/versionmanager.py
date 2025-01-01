#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Generic, Iterable, Iterator, Optional, Sequence, Type, TypeVar, Tuple, Union
from typing import ItemsView, KeysView, ValuesView
from typing import Any, List, Dict, Set
from typing import cast, overload
import builtins
from xpl import Builtins
from .semanticversiondata import SemanticVersionData


#--------------------------------------------------------------------------------
# 전역 상수 목록.
#--------------------------------------------------------------------------------
UTF8: str = "utf-8"
FILE_READTEXT: str = "rt"
FILE_WRITETEXT: str = "wt"


#--------------------------------------------------------------------------------
# 버전 매니저.
#--------------------------------------------------------------------------------
class VersionManager:
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	__semanticVersionData: SemanticVersionData


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		self.__semanticVersionData = SemanticVersionData()


	#--------------------------------------------------------------------------------
	# 실행.
	#--------------------------------------------------------------------------------
	@staticmethod
	def CreateVersionToFile(versionFilePath: str) -> None:
		with builtins.open(versionFilePath, mode = FILE_WRITETEXT, encoding = UTF8) as file:
			file.write()


	#--------------------------------------------------------------------------------
	# 버전 문자열로 버전 데이터 생성.
	#--------------------------------------------------------------------------------
	@staticmethod
	def CreateSemanticVersionDataFromVersionString(versionString: str) -> SemanticVersionData:
		semanticVersionData = SemanticVersionData()
		values = versionString.split(".")
		semanticVersionData.SetSemanticVersion(int(values[0]), int(values[1]), int(values[2]))
		return semanticVersionData


	#--------------------------------------------------------------------------------
	# 버전 문자열 파일로 버전 데이터 생성.
	#--------------------------------------------------------------------------------
	@staticmethod
	def CreateSemanticVersionDataFromVersionStringFile(versionFilePath: str) -> SemanticVersionData:
		with builtins.open(versionFilePath, mode = FILE_READTEXT, encoding = UTF8) as file:
			versionString: str = file.read()
			return VersionManager.CreateSemanticVersionDataFromVersionString(versionString)
