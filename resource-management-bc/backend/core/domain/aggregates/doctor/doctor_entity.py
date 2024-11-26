from uuid import uuid4

from core.domain.common.base_entity import BaseEntity


# Aggregate root
class DoctorEntity(BaseEntity):
    def __init__(self, doctor_id: int, name: str, specialization: str):
        super.__init__(doctor_id)
        self.name = name
        self.specialization = specialization

    def __repr__(self):
        return f"Doctor(id='{self.id}', name='{self.name}', specialization='{self.specialization}')"

    @classmethod
    def register_doctor(cls, name: str, specialization: str):
        return cls(doctor_id=uuid4().hex, name=name, specialization=specialization)
