from sqlalchemy.orm import Session
from core.domain.entities.client.client_entity import ClientEntity
from .client_repository import ClientRepository

class SQLAlchemyClientRepository(ClientRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, client: ClientEntity) -> None:
        self.session.add(client)
        self.session.commit()

    def get_by_id(self, client_id: str) -> ClientEntity:
        return self.session.query(ClientEntity).filter_by(id=client_id).first()

    def get_all(self) -> list[ClientEntity]:
        return self.session.query(ClientEntity).all()
