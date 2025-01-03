import typing


class KeyStorage:
    @classmethod
    def get(cls) -> typing.Optional[str]:
        return None

    @classmethod
    def set(cls, key: str) -> None:
        pass

    @classmethod
    def is_available(cls) -> bool:
        raise NotImplementedError()  # pragma: no cover

    @staticmethod
    def get_storage() -> typing.Type["KeyStorage"]:
        for subclass in KeyStorage.__subclasses__():
            if subclass.is_available():
                return subclass

        return KeyStorage
