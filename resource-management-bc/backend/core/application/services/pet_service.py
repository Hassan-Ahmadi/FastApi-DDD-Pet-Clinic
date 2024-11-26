from core.domain.entities import Pet
from core.domain.repositories import PetRepository

class PetService:
    def __init__(self, pet_repository: PetRepository):
        self.pet_repository = pet_repository

    def create_pet(self, name: str, owner: Client, pet_type: str) -> Pet:
        pet = Pet(name=name, owner=owner, pet_type=pet_type)
        self.pet_repository.save(pet)
        return pet

    def get_pet_by_id(self, pet_id: str) -> Pet:
        return self.pet_repository.get_by_id(pet_id)