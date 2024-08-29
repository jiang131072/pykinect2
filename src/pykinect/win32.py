from ctypes import Structure, windll
from ctypes.wintypes import (
    BOOL,
    DWORD,
    HANDLE,
    LPCWSTR,
    LPVOID,
    POINTER,
)


class SECURITY_ATTRIBUTES(Structure):
    _fields_ = [
        ("nLength", DWORD),
        ("lpSecurityDescriptor", LPVOID),
        ("bInheritHandle", BOOL),
    ]


LPSECURITY_ATTRIBUTES = POINTER(SECURITY_ATTRIBUTES)

CreateEventW = windll.Kernel32.CreateEventW
CreateEventW.argtypes = [LPSECURITY_ATTRIBUTES, BOOL, BOOL, LPCWSTR]
CreateEventW.restype = HANDLE

CloseHandle = windll.Kernel32.CloseHandle
CloseHandle.argtypes = [HANDLE]
CloseHandle.restype = BOOL

WaitForMultipleObjects = windll.Kernel32.WaitForMultipleObjects
WaitForMultipleObjects.argtypes = [DWORD, POINTER(HANDLE), BOOL, DWORD]
WaitForMultipleObjects.restype = DWORD
