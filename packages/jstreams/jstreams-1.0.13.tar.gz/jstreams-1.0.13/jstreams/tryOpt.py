from typing import TypeVar, Callable, Optional, Any, Generic, Protocol

from jstreams.stream import Opt

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")

class ErrorLog(Protocol):
    def error(self, msg, *args, **kwargs):  # type: ignore[no-untyped-def]
        pass


class Try(Generic[T]):
    __slots__ = ("__fn", "__thenChain", "__onFailure", "__errorLog", "__errorMessage", "__hasFailed")

    def __init__(self, fn: Callable[[], T]):
        self.__fn = fn
        self.__thenChain: list[Callable[[T], Any]] = []
        self.__onFailure: Optional[Callable[[BaseException], Any]] = None
        self.__errorLog: Optional[ErrorLog] = None
        self.__errorMessage: Optional[str] = None
        self.__hasFailed = False

    def andThen(self, fn: Callable[[T], Any]) -> "Try[T]":
        self.__thenChain.append(fn)
        return self

    def onFailure(self, fn: Callable[[BaseException], Any]) -> "Try[T]":
        self.__onFailure = fn
        return self

    def onFailureLog(self, message: str, errorLog: ErrorLog) -> "Try[T]":
        self.__errorLog = errorLog
        self.__errorMessage = message
        return self

    def get(self) -> Opt[T]:
        try:
            val = self.__fn()
            for fn in self.__thenChain:
                fn(val)
            return Opt(val)
        except Exception as e:
            self.__hasFailed = True
            if self.__onFailure is not None:
                self.__onFailure(e)
            if self.__errorLog is not None and self.__errorMessage is not None:
                self.__errorLog.error(self.__errorMessage)  # type: ignore[no-untyped-call]
                self.__errorLog.error(e, exc_info=True)  # type: ignore[no-untyped-call]
        return Opt(None)

    def hasFailed(self) -> bool:
        self.get()
        return self.__hasFailed
    
    @staticmethod
    def of(val: K) -> "Try[K]":
        return Try(lambda: val)
