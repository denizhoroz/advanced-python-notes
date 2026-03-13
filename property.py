class Something:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """The value property."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Set the value property."""
        if new_value < 0:
            raise ValueError("Value cannot be negative.")
        self._value = new_value


thing = Something(10)
print(thing.value)  # Output: 10

thing.value = 20
print(thing.value)  # Output: 20