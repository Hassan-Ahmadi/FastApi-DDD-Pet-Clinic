from uuid import uuid4

from core.common.base_entity import BaseEntity
from core.domain.aggregates.client.client_entity import ClientEntity
from core.domain.aggregates.doctor.doctor_entity import DoctorEntity

# Aggregate root: Clinic
class AppointmentEntity(BaseEntity):
    def __init__(self, appointment_id: int, client: ClientEntity, doctor: DoctorEntity) -> None:
        super().__init__(room_id)
        self.name = name

    def __repr__(self):
        return f"Room(id='{self.id}', name='{self.name}')"

    @classmethod
    def register_room(cls, name: str):
        return cls(room_id=uuid4().hex, name=name)
