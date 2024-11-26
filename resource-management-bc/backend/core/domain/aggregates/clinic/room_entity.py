from uuid import uuid4

from core.common.base_entity import BaseEntity

# Aggregate root: Clinic
class RoomEntity(BaseEntity):
    def __init__(self, room_id: int, name: str) -> None:
        super().__init__(room_id)
        self.name = name

    def __repr__(self):
        return f"Room(id='{self.id}', name='{self.name}')"

    @classmethod
    def register_room(cls, name: str):
        return cls(room_id=uuid4().hex, name=name)
