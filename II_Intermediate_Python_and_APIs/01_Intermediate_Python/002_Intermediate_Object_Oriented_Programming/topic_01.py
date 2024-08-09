class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Elephant(Animal):
    pass


bubbles_the_elephant = Elephant("Bubbles", 2)
bubbles_the_elephant.display()
