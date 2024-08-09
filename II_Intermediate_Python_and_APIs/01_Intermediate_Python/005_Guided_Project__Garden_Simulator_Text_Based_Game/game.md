# Grow a Garden!

* Players will simulate the experience of gardening by planting, growing, and
  harvesting virtual plants.

* Players will choose which plants to grow, tend to them, and eventually harvest them.

* The game will incorporate various stages of plant growth, from seeds to mature
  plants, and players will need to care for their plants at each stage.

Features:

* Planting: Choose a plant from your inventory and plant it.
* Tending: Care for your plants to help them grow.
* Harvesting: Once a plant is mature, harvest it to add to your inventory.
* Foraging: Look for new seeds to expand your plant collection.

Let's start by importing the `random` library so we can include some unpredictability
for elements in the game.

```python
import random
```

## The Plant Class

### Creating the Plant Class and Attributes

This class represents the base Plant in the garden, with attributes to define the
plant's `name`, the amount of fruits or vegetables that can be harvested from a mature
plant as `harvest_yield`, the growth stages this plant goes through, the current
growth stage, and whether or not the plant is currently `harvestable`.

### Adding Methods to the Plant Class

The Plant class has two methods: `grow` and `harvest`.

* `grow()`: updates the plant's `current_growth_stage` attribute if it is not already
  on the final growth stage. If the plant is ready for harvest, this method also
  updates the `harvestable` attribute to `True`.

* `harvest()`: Sets the `harvestable` attribute to `False` and returns the
  `harvest_yield`. The remainder of harvest-related actions will happen in the
  `Gardener` class

```python
class Plant:
    def __init__(self, name, harvest_yield):
        self.name = name
        self.harvest_yield = harvest_yield
        self.growth_stages = [
            "seed",
            "sprout",
            "mature",
            "flower",
            "fruit",
            "harvest-ready",
        ]
        self.current_growth_stage = self.growth_stages[
            0
        ]  # Initial growth stage is seed
        self.harvestable = False

    def grow(self):
        current_index = self.growth_stages.index(self.current_growth_stage)
        if self.current_growth_stage == self.growth_stages[-1]:
            print(f"{self.name} is already fully grown!")
        elif current_index < len(self.growth_stages) - 1:
            self.current_growth_stage = self.growth_stages[current_index + 1]
            if self.current_growth_stage == "harvest-ready":
                self.harvestable = True

    def harvest(self):
        if self.harvestable:
            self.harvestable = False
            return self.harvest_yield
        else:
            return None
```

## Define Specific Plant Types

Plant subclasses will be the heart of the game, representing as many plants as we want
to create subclasses for. Below, we can see that the `Tomato` subclass inherits
everything from `Plant`, but `Lettuce` and `Carrot` override the inherited
`growth_stages` attribute because these types of plant do not flower or fruit before
they are "harvest-ready."

```python
class Tomato(Plant):
    def __init__(self):
        super().__init__("Tomato", 10)


class Lettuce(Plant):
    def __init__(self):
        super().__init__("Lettuce", 5)
        self.growth_stages = ["seed", "sprout", "mature", "harvest-ready"]


class Carrot(Plant):
    def __init__(self):
        super().__init__("Carrot", 8)
        self.growth_stages = ["seed", "sprout", "mature", "harvest-ready"]
```

## Selecting Inventory Items

This is a helper function that will go through a dictionary or list, display the keys
or list items to the user as a numbered list, and then prompt the user to select an
item by number. The function returns the corresponding item.

### Continuous Prompting for Selecting Items

An important aspect of this helper function is its ability to continuously prompt
users until they select valid input. This helps account for input errors and ensures
that users provide valid selections.

```python
def select_item(items):
    # Determine if items is a dictionary or a list
    if type(items) == dict:
        item_list = list(items.keys())
    elif type(items) == list:
        item_list = items
    else:
        print("Invalid items type.")
        return None
    # Print out the items
    for i in range(len(item_list)):
        try:
            item_name = item_list[i].name
        except:
            item_name = item_list[i]
        print(f"{i + 1}. {item_name}")

    # Get user input
    while True:
        user_input = input("Select an item: ")
        try:
            user_input = int(user_input)
            if 0 < user_input <= len(item_list):
                return item_list[user_input - 1]
            else:
                print("Invalid input.")
        except:
            print("Invalid input.")
```

## Defining the Gardener Class

The `Gardener` class models the player, who can plant, tend, harvest, and forage
plants. The class has three attributes:

* `name` represents the gardener's name
* `planted_plants` is a list of any plants the gardener has currently planted
* `inventory` is a dictionary where the keys are the item names and the values are the
  quantity of the item.

We have also created a `plant_dict` before the `__init__` method to connect each plant
subclass to a string so that it is easier to instantiate new objects for each type.

### Extending the Gardener Class Functionality

The `Gardener` class has four methods:

* `plant()`: This method allows the gardener to plant a plant from their inventory. It
  prompts the user to select a plant from their inventory, then adds the plant to the
  `planted_plants` list and removes it from the `inventory` dictionary.

* `tend()`: This method allows the gardener to tend to their plants. It prompts the
  user to select a plant from their planted plants, then calls the `grow()` method on
  that plant.

* `harvest()`: This method allows the gardener to harvest a plant. It prompts the user
  to select a plant from their planted plants, then calls the `harvest()` method on
  that plant. It then adds the harvest yield to the gardener's inventory.

### Introducing Randomness: Foraging for Seeds

The `forage()` method allows the gardener to forage for seeds. It randomly selects a
plant type from the `plant_dict` and adds it to the gardener's inventory.

```python
class Gardener:
    """Represents a gardener who can plant and harvest plants."""

    plant_dict = {"tomato": Tomato, "lettuce": Lettuce, "carrot": Carrot}

    def __init__(self, name):
        self.name = name
        self.planted_plants = []
        self.inventory = {}

    def plant(self):
        selected_plant = select_item(self.inventory)
        if selected_plant in self.inventory and self.inventory[selected_plant] > 0:
            self.inventory[selected_plant] -= 1
            if self.inventory[selected_plant] == 0:
                del self.inventory[selected_plant]
            new_plant = self.plant_dict[selected_plant]()
            self.planted_plants.append(new_plant)
            print(f"{self.name} planted a {selected_plant}!")
        else:
            print(f"{self.name} doesn't have any {selected_plant} to plant!")

    def tend(self):
        for plant in self.planted_plants:
            if plant.harvestable:
                print(f"{plant.name} is ready to be harvested!")
            else:
                plant.grow()
                print(f"{plant.name} is now a {plant.current_growth_stage}!")

    def harvest(self):
        selected_plant = select_item(self.planted_plants)
        if selected_plant.harvestable == True:
            if selected_plant.name in self.inventory:
                self.inventory[selected_plant.name] += selected_plant.harvest()
            else:
                self.inventory[selected_plant.name] = selected_plant.harvest()
            print(f"You harvested a {selected_plant.name}!")
            self.planted_plants.remove(selected_plant)
        else:
            print(f"You can't harvest a {selected_plant.name}!")

    def forage_for_seeds(self):
        seed = random.choice(all_plant_types)
        if seed in self.inventory:
            self.inventory[seed] += 1
        else:
            self.inventory[seed] = 1
        print(f"{self.name} found a {seed} seed!")
```

## Setting Up the Main Game Loop

The main game loop will be the core of the game, where the player can choose what
actions to take. The loop will continue until the player chooses to quit the game.

### Setting Game-Level Variables

We will need to set up some variabels to keep track of contants in the game.
`all_plant_types` is a list of all the plant types we have created. `valid_commands`
is a list of all the commands the player can use. There is also a `gardener_name`
variable that collects the player's name and a `gardener` variable that will be used
to instantiate the `Gardener` class.

There is also print statements that welcome the player to the game and explain the
commands.

```python
all_plant_types = ["tomato", "lettuce", "carrot"]
valid_commands = ["plant", "tend", "harvest", "forage", "help", "quit"]

# Print welcome message
print(
    "Welcome to the garden! You will act as a virtual gardener.\n"
    "Forage for new seeds, plant them, and then watch them grow!\n"
    "Start by entering your name."
)

# Create gardener
gardener_name = input("What is your name? ")
print(
    f"Welcome, {gardener_name}! Let's get gardening!\nType 'help' for a list of commands."
)
gardener = Gardener(gardener_name)
```

### The Main Game Loop

The main game loop will continue until the player chooses to quit the game. The loop
will prompt the player to enter a command, then call the appropriate method on the
`Gardener` class.

```python
# Main game loop
while True:
    player_action = input("What would you like to do? ")
    player_action = player_action.lower()
    if player_action in valid_commands:
        if player_action == "plant":
            gardener.plant()
        elif player_action == "tend":
            gardener.tend()
        elif player_action == "harvest":
            gardener.harvest()
        elif player_action == "forage":
            gardener.forage_for_seeds()
        elif player_action == "help":
            print("*** Commands ***")
            for command in valid_commands:
                print(command)
        elif player_action == "quit":
            print("Goodbye!")
            break
    else:
        print("Invalid command.")
```

# Gameplay Example

```plaintext
Welcome to the garden! You will act as a virtual gardener.
Forage for new seeds, plant them, and then watch them grow!
Start by entering your name.
What is your name?  Jane Doe
Welcome, Jane Doe! Let's get gardening!
Type 'help' for a list of commands.
What would you like to do?  help
*** Commands ***
plant
tend
harvest
forage
help
quit
What would you like to do?  forage
Jane Doe found a tomato seed!
What would you like to do?  plant
1. tomato
Select an item:  1
Jane Doe planted a tomato!
What would you like to do?  tend
Tomato is now a sprout!
What would you like to do?  tend
Tomato is now a mature!
What would you like to do?  tend
Tomato is now a flower!
What would you like to do?  tend
Tomato is now a fruit!
What would you like to do?  tend
Tomato is now a harvest-ready!
What would you like to do?  harvest
1. Tomato
Select an item:  1
You harvested a Tomato!
What would you like to do?  quit
Goodbye!
```
