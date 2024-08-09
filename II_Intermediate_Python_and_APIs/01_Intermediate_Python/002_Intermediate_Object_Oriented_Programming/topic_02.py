class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Elephant(Animal):
    def __init__(self, name, age, trunk_length):
        super().__init__(name, age)
        self.trunk_length = trunk_length
        self.description = f"{self.name} has a trunk {self.trunk_length} meters long."


bubbles_the_elephant = Elephant("Bubbles", 2, 1.83)
print(bubbles_the_elephant.description)
