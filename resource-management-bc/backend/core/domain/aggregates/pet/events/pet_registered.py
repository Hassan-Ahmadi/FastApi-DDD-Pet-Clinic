from core.common.base_domain_event import BaseDomainEvent

class PetRegisteredEvent(BaseDomainEvent):
    """An event representing the registration of a pet. """
    
    def __init__(self, pet_id: str, name: str) -> None:
        super().__init__()
        self.pet_id = pet_id
        self.name = name

    @property
    def version(self) -> int:
        return 1

    @property
    def event_type(self) -> str:
        return "pet_registered"
