#--------------------------------------------------------------------------------
# 참조 모듈 목록.
#--------------------------------------------------------------------------------
from __future__ import annotations
from typing import Awaitable, Callable, Final, Generic, Iterable, Iterator, Optional, Sequence, Type, TypeVar, Tuple, Union
from typing import ItemsView, KeysView, ValuesView
from typing import Any, List, Dict, Set
from typing import cast, overload
import builtins
from xpl import Builtins, BaseClass
from .versiondata import VersionData


#--------------------------------------------------------------------------------
# 시맨틱 버전 데이터.
# - Major.Minor.Patch의 3가지 단계적 숫자로 구분하는 표준 표기법을 사용.
#--------------------------------------------------------------------------------
class SemanticVersionData(VersionData):
	#--------------------------------------------------------------------------------
	# 멤버 변수 목록.
	#--------------------------------------------------------------------------------
	__major: int
	__minor: int
	__patch: int


	#--------------------------------------------------------------------------------
	# 메이저 버전.
	#--------------------------------------------------------------------------------
	@property
	def Major(self) -> int:
		return self.__major


	#--------------------------------------------------------------------------------
	# 메이저 버전.
	#--------------------------------------------------------------------------------
	@Major.setter
	def Major(self, value: int) -> None:
		self.__major = value
		self.SetSemanticVersion(self.__major, self.__minor, self.__patch)
	

	#--------------------------------------------------------------------------------
	# 마이너 버전.
	#--------------------------------------------------------------------------------
	@property
	def Minor(self) -> int:
		return self.__minor


	#--------------------------------------------------------------------------------
	# 마이너 버전.
	#--------------------------------------------------------------------------------
	@Minor.setter
	def Minor(self, value: int) -> None:
		self.__minor = value
		self.SetSemanticVersion(self.__major, self.__minor, self.__patch)

	
	#--------------------------------------------------------------------------------
	# 패치 버전.
	#--------------------------------------------------------------------------------
	@property
	def Patch(self) -> int:
		return self.__patch


	#--------------------------------------------------------------------------------
	# 패치 버전.
	#--------------------------------------------------------------------------------
	@Patch.setter
	def Patch(self, value: int) -> None:
		self.__patch = value
		self.SetSemanticVersion(self.__major, self.__minor, self.__patch)


	#--------------------------------------------------------------------------------
	# 생성됨.
	#--------------------------------------------------------------------------------
	def __init__(self) -> None:
		self.__major: int = 0
		self.__minor: int = 0
		self.__patch: int = 0
		self.SetSemanticVersion(0, 0, 0)


	#--------------------------------------------------------------------------------
	# 기본 버전 초기화. (0.0.0)
	#--------------------------------------------------------------------------------
	def ResetVersion(self) -> None:
		# 기본 버전 초기화.
		# base = super()
		# base.ResetVersion()

		# 시맨틱 버전 초기화.
		self.SetSemanticVersion(0, 0, 0)


	#--------------------------------------------------------------------------------
	# 기본 버전 설정.
	#--------------------------------------------------------------------------------
	def SetVersion(self, version: str) -> None:
		# 기본 버전 설정.
		# base = super()
		# base.SetVersion(f"{major}.{minor}.{patch}")
		try:
			# 버전 분리.
			separator: str = "."
			values = version.split(separator)
			major: int = int(values[0])
			minor: int = int(values[1])
			patch: int = int(values[2])

			# 시맨틱 버전 설정.
			self.SetSemanticVersion(major, minor, patch)

		except Exception as exception:
			# 시맨틱 버전 초기화.
			self.ResetVersion()
			raise


	#--------------------------------------------------------------------------------
	# 시맨틱 버전 설정.
	#--------------------------------------------------------------------------------
	def SetSemanticVersion(self, major: int, minor: int, patch: int) -> None:
		# 기본 버전 설정.
		base = super()
		base.SetVersion(f"{major}.{minor}.{patch}")

		# 시맨틱 버전 설정.
		self.__major = major
		self.__minor = minor
		self.__patch = patch