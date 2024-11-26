from domain.common.value_obj import ValueObject

class SmapleVO(ValueObject):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self):
        return f"SampleVO(name='{self.name}', age='{self.age}')"
