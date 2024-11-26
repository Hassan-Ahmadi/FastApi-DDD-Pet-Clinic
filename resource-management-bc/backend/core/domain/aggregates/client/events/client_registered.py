from core.common.base_domain_event import BaseDomainEvent

class ClientRegisteredEvent(BaseDomainEvent):
    """An event representing the registration of a client. """
    
    def __init__(self, client_id: str, name: str, phone_number: str) -> None:
        super().__init__()
        self.client_id = client_id
        self.name = name
        self.phone_number = phone_number

    @property
    def version(self) -> int:
        return 1

    @property
    def event_type(self) -> str:
        return "client_registered"
