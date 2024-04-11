from typing import List, Optional


class UserProvidedConfig:
    def __init__(self, name: str, port: int,
                 replicas: int, cloud: str) -> None: ...


class Dispatcher:
    def __init__(self) -> None: ...

    def add_service(self, name: str,
                    config: Optional[UserProvidedConfig]) -> None: ...

    def remove_service(self, name: str) -> None: ...

    def up(self, name: str) -> None: ...

    def down(self, name: str) -> None: ...

    def status(self, name: str, pretty: Optional[bool]) -> str: ...

    def save(self) -> None: ...

    def save_as_b64(self) -> str: ...

    def load(self, name: str) -> None: ...

    def load_as_b64(self, b64: str) -> None: ...

    def list(self) -> List[str]: ...