from sqlalchemy.orm import Session
from core.domain.entities import Pet
from core.domain.repositories import PetRepository

class SQLAlchemyPetRepository(PetRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, pet: Pet) -> None:
        self.session.add(pet)
        self.session.commit()

    def get_by_id(self, pet_id: str) -> Pet:
        return self.session.query(Pet).filter_by(id=pet_id).first()