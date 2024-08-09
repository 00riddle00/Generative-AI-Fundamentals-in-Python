class Elephant:
    def __init__(self, favorite_food, friendliness):
        self.favorite_food = favorite_food
        self.friendliness = friendliness
        self.updates = 0

    def trumpet(self):
        return "Toot toot!"

    def remember(self, memory_list):
        return memory_list

    def improve_friendliness(self, friendliness_boost):
        self.friendliness += friendliness_boost
        self.updates += 1


bubbles = Elephant("watermelon", 70)
print(bubbles.updates)

bubbles.improve_friendliness(10)
print(bubbles.updates)
