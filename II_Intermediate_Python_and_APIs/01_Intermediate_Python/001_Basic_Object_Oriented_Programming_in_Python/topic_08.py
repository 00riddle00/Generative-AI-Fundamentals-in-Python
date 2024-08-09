class Elephant:
    def __init__(self, favorite_food, friendliness):
        self.favorite_food = favorite_food
        self.friendliness = friendliness

    def trumpet(self):
        return "Toot toot!"

    def remember(self, memory_list):
        return memory_list


bubbles = Elephant("watermelon", 70)
print(bubbles.favorite_food)
print(bubbles.friendliness)
