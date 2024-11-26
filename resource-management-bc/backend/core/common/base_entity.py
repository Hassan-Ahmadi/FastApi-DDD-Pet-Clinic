from abc import ABCMeta, abstractmethod


class BaseEntity(metaclass=ABCMeta):
    """The base class of all entities.
    
    Attributes:
        id: A unique idenifier.
        instance_id: A value unique among instances of this entity.
        version: An integer version.
        discarded: True if this entity should no longer be used,
            itherwise False

    """
    @abstractmethod
    def __init__(self, entity_id) -> None:
        self.id = entity_id
        self._discarded = False

    def _check_not_discarded(self):
        if self._discarded:
            raise DiscardedEntityError("Attemp to use {}".format(repr(self)))

    def __eq__(self, other: object) -> bool:
        return isinstance(other, BaseEntity) and other.id == self.id

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)


class DiscardedEntityError(Exception):
    """Raised when an attempt is madeto use a discarded Entity. """
    pass
