from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    tags: list = field(default_factory=list)
    active: bool = field(default=True)


person1 = Person(name="Alice", age=30)
print(person1)