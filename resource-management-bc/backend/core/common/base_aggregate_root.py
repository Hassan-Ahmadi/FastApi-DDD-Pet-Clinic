from .base_entity import BaseEntity


class BaseAggregateRoot(BaseEntity):

    def __init__(self, entity_id) -> None:
        super().__init__(entity_id)
        self._events = []

    @property
    def events(self) -> None:
        return self._events
