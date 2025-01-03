import os
import typing
import python_linux_keyutils

from .main import KeyStorage


class LinuxKernelKeyStorage(KeyStorage):
    @classmethod
    def get_secret_name(cls):
        return os.environ.get("TG_BW_SESSION_SECRET_NAME", "")

    @classmethod
    def is_available(cls) -> bool:
        return bool(cls.get_secret_name())

    @classmethod
    def get(cls) -> typing.Optional[str]:
        try:
            result = python_linux_keyutils.get_secret(cls.get_secret_name())
        except (KeyError, ValueError, RuntimeError):
            return None

        try:
            session_token = result.decode()
            return session_token or None
        except UnicodeDecodeError:
            return None

    @classmethod
    def set(cls, key: str) -> None:
        try:
            python_linux_keyutils.set_secret(cls.get_secret_name(), key.encode())
        except (KeyError, ValueError, RuntimeError):
            pass
