from abc import ABC, abstractmethod
from flask import current_app


class BaseService(ABC):
    def __init__(self) -> None:
        self.logger = current_app.logger


class BaseInputCapture(BaseService, ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def update(self) -> None:
        pass
