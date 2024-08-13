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

    def age_up(self):
        self.age += 1
        self._check_retirement()

    def _check_retirement(self):
        if self.age >= 10:
            print(f"{self.name} has retired.")

    def move(self):
        pass


class Elephant(Animal):
    def __init__(self, name, age, trunk_length):
        super().__init__(name, age)
        self._trunk_length = trunk_length
        self.description = f"{self.name} has a trunk {self._trunk_length} meters long."

    def _use_trunk(self):
        if self.age < 1 or self._trunk_length < 1.2:
            return False
        return True

    def eat(self):
        super().eat()
        if self._use_trunk():
            print(f"{self.name} is munching on some leaves with its trunk!")
        else:
            print(f"{self.name} struggles to use its trunk, so it eats differently.")

    def move(self):
        print(f"{self.name} is stomping!")

    def get_trunk_length(self):
        return self._trunk_length

    def set_trunk_length(self, length):
        if 0 < length < 3:
            self._trunk_length = length
        else:
            print("Trunk length must be between 0 and 3 meters.")


bubbles_the_elephant = Elephant("Bubbles", 2, 1.83)
tiny_the_elephant = Elephant("Tiny", 0, 0.8)

bubbles_the_elephant.eat()
tiny_the_elephant.eat()
