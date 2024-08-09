class Elephant:
    def trumpet(self):
        return "Toot toot!"

    def remember(self, memory_list):
        return memory_list


bubbles = Elephant()
bubbles_recalled_objects = bubbles.remember(["ball", "bucket", "tree"])
