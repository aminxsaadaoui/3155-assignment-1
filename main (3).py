### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item, amount in ingredients.items():
            if self.machine_resources[item] < amount:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        total = 0
        total += int(input("How many large dollars?: ")) * 1.0
        total += int(input("How many half dollars?: ")) * 0.5
        total += int(input("How many quarters?: ")) * 0.25
        total += int(input("How many nickels?: ")) * 0.05
        return total

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif coins > cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    def report(self):
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} ounce(s)")

### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)
def run_machine():
    while True:
        choice = input("What would you like? (small/medium/large/off/report): ").lower()

        if choice == "off":
            print("Turning off the machine.")
            break
        elif choice == "report":
            machine.report()
        elif choice in ["small", "medium", "large"]:
            sandwich = recipes[choice]
            if machine.check_resources(sandwich["ingredients"]):
                payment = machine.process_coins()
                if machine.transaction_result(payment, sandwich["cost"]):
                    machine.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("Invalid selection. Please choose again.")
run_machine()