from core.domain.entities import Client
from core.domain.repositories import ClientRepository

class ClientService:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository


    def create_client(self, name: str, phone_number: str) -> Client:
        client = Client(name=name, phone_number=phone_number)
        self.client_repository.save(client)
        return client

    def get_client_by_id(self, client_id: str) -> Client:
        return self.client_repository.get_by_id(client_id)