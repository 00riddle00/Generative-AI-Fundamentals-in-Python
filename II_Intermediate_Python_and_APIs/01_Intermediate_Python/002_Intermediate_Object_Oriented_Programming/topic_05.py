class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def eat(self):
        print(f"This animal is eating.")

    def move(self):
        pass


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


class Lion(Animal):
    def __init__(self, name, age, mane_color):
        super().__init__(name, age)
        self.mane_color = mane_color

    def move(self):
        print(f"{self.name} is prowling!")


bubbles_the_elephant = Elephant("Bubbles", 2, 1.83)
leo_the_lion = Lion("Leo", 5, "golden")

all_animals = [bubbles_the_elephant, leo_the_lion]

for animal in all_animals:
    animal.move()
