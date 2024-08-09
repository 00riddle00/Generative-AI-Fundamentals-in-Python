class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._is_hungry = True
        self._is_tired = True

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def eat(self):
        print(f"This animal is eating.")
        self._is_hungry = False

    def move(self):
        pass

    def sleep(self):
        self._is_tired = False


class Elephant(Animal):
    def __init__(self, name, age, trunk_length):
        super().__init__(name, age)
        self.trunk_length = trunk_length
        self.description = f"{self.name} has a trunk {self.trunk_length} meters long."

    def eat(self):
        super().eat()
        print(f"{self.name} is munching on some leaves!")

    def move(self):
        print(f"{self.name} is stomping!")


bubbles_the_elephant = Elephant("Bubbles", 2, 1.83)
bubbles_the_elephant.sleep()
print(bubbles_the_elephant._is_tired)
