from abc import ABC, abstractmethod
from datetime import datetime
from uuid import uuid4


class BaseDomainEvent(ABC):
    def __init__(self, occurred_on: datetime = None):
        self.id = str(uuid4())
        self.occurred_on = occurred_on or datetime.now()

    @property
    @abstractmethod
    def version(self) -> int:
        pass

    @property
    @abstractmethod
    def event_type(self) -> str:
        pass
