from uuid import uuid4

from core.common.base_aggregate_root import BaseAggregateRoot
# from .room_entity import RoomEntity
from .app import ScheduleEntity


# Aggregate root
class ScheduleEntity(BaseAggregateRoot):
    def __init__(self, appointments) -> None:
        super().__init__(clinic_id)
        self.name = name
        self.rooms = rooms

    def __repr__(self):
        return f"Clinic(id='{self.id}', name='{self.name}')"

    @classmethod
    def register_clinic(cls, name: str, rooms: list[RoomEntity]):
        return cls(clinic_id=uuid4().hex, name=name, rooms=rooms)
