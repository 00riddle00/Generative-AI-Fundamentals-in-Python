class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._is_hungry = True

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def eat(self):
        print("This animal is eating.")
        self._is_hungry = False

    def move(self):
        pass


class Elephant(Animal):
    def __init__(self, name, age, trunk_length):
        super().__init__(name, age)
        self._trunk_length = trunk_length
        self.description = f"{self.name} has a trunk {self._trunk_length} meters long."

    def eat(self):
        super().eat()
        print(f"{self.name} is munching on some leaves!")

    def move(self):
        print(f"{self.name} is stomping!")

    def get_trunk_length(self):
        return self._trunk_length

    def set_trunk_length(self, value):
        if 0 < value < 3:
            self._trunk_length = value
        else:
            print("Error: Trunk length must be between 0 and 3 meters.")


bubbles_the_elephant = Elephant("Bubbles", 2, 1.83)
print(bubbles_the_elephant.get_trunk_length())

bubbles_the_elephant.set_trunk_length(3.5)
print(bubbles_the_elephant.get_trunk_length())

bubbles_the_elephant.set_trunk_length(2.5)
print(bubbles_the_elephant.get_trunk_length())
