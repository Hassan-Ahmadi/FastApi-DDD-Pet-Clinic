from uuid import uuid4

from core.domain.common.base_entity import BaseEntity
from core.domain.entities.client.client_entity import Client


# Aggregate root
class PetEntity(BaseEntity):
    def __init__(self, pet_id: int, name: str, owner: Client) -> None:
        super().__init__(pet_id)
        self.name = name
        self.owner = owner

    def __repr__(self):
        return f"Pet(id='{self.id}', name='{self.name}', owner='{self.owner}'"

    @classmethod
    def register_pet(cls, name: str, owner: Client):
        return cls(pet_id=uuid4().hex, name=name, owner=owner)
