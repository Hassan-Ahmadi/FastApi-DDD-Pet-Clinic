from abc import ABC, abstractmethod
from .client_entity import ClientEntity


class ClientRepository(ABC):
    @abstractmethod
    def save(self, client: ClientEntity) -> None:
        """Saves a client to the data store."""
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, client_id: str) -> ClientEntity:
        """Retrieves a client by its ID."""
        raise NotImplementedError

    @abstractmethod
    def get_by_name(self, name: str) -> ClientEntity:
        """Retrieves a client by its ID."""
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[ClientEntity]:
        """Retrieves all clients."""
        raise NotImplementedError
