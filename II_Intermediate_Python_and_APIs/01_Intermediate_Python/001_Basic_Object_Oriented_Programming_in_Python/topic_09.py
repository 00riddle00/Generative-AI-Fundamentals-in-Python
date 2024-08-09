class Elephant:
    def __init__(self, favorite_food, friendliness):
        self.favorite_food = favorite_food
        self.friendliness = friendliness

    def trumpet(self):
        return "Toot toot!"

    def remember(self, memory_list):
        return memory_list

    # Add method here
    def improve_friendliness(self, friendliness_boost):
        self.friendliness += friendliness_boost


bubbles = Elephant("watermelon", 70)

print(bubbles.favorite_food)
print(bubbles.friendliness)

bubbles.improve_friendliness(20)
print(bubbles.friendliness)
