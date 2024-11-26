from uuid import uuid4

from core.common.base_aggregate_root import BaseAggregateRoot


class ClientEntity(BaseAggregateRoot):
    def __init__(self, client_id: int, name: str, phone_number: str) -> None:
        super().__init__(client_id)
        self.name = name
        self.phone_number = phone_number

    def __repr__(self):
        return f"Client(id='{self.id}', name='{self.name}', phone_number='{self.phone_number}'"

    @classmethod
    def register_client(cls, name, phone_number):
        return cls(client_id=uuid4().hex, name=name, phone_number=phone_number)
