class CoffeeMachine:

    def __init__(self, water, milk, c_beans, cups, money):
        self.water = water
        self.milk = milk
        self.c_beans = c_beans
        self.cups = cups
        self.money = money

    def __str__(self):
        return (f"\n"
                f"The coffee machine has:\n"
                f"{self.water} of water\n"
                f"{self.milk} of milk\n"
                f"{self.c_beans} of coffee beans\n"
                f"{self.cups} of disposable cups\n"
                f"${self.money} of money")

    def buy(self):
        choose = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu\n', )
        if choose == '1':
            coffee = [250, 0, 16, 1, 4]
            CoffeeMachine.check_ingredients(self, coffee)
        elif choose == '2':
            coffee = [350, 75, 20, 1, 7]
            CoffeeMachine.check_ingredients(self, coffee)
        elif choose == '3':
            coffee = [200, 100, 12, 1, 6]
            CoffeeMachine.check_ingredients(self, coffee)

    def check_ingredients(self, coffee):
        if self.water > coffee[0]:
            if self.milk > coffee[1]:
                if self.c_beans > coffee[2]:
                    if self.cups > coffee[3]:
                        self.water = self.water - coffee[0]
                        self.milk = self.milk - coffee[1]
                        self.c_beans = self.c_beans - coffee[2]
                        self.cups = self.cups - coffee[3]
                        self.money = self.money + coffee[4]
                        print('I have enough resources, making you a coffee!\n')
                    else:
                        print('Sorry, not enough cups!\n')
                else:
                    print('Sorry, not enough coffee beans!\n')
            else:
                print('Sorry, not enough milk!\n')
        else:
            print('Sorry, not enough water!\n')

    def fill(self):
        ingredient_fill = int(input('\nWrite how many ml of water do you want to add:\n', ))
        self.water = self.water + ingredient_fill
        ingredient_fill = int(input('Write how many ml of milk do you want to add::\n', ))
        self.milk= self.milk + ingredient_fill
        ingredient_fill = int(input('Write how many grams of coffee beans do you want to add:\n', ))
        self.c_beans = self.c_beans + ingredient_fill
        ingredient_fill = int(input('Write how many disposable cups of coffee do you want to add:\n', ))
        self.cups = self.cups + ingredient_fill

    def take(self):
        print(f'\nI gave you ${self.money}')
        self.money = self.money - self.money


def main_options(coffee_machine):
    while True:
        action = input('\nWrite action (buy, fill, take, remaining, exit):\n')
        if action == 'buy':
            coffee_machine.buy()
        elif action == 'fill':
            coffee_machine.fill()
        elif action == 'take':
            coffee_machine.take()
        elif action == 'remaining':
            print(coffee_machine.__str__())
        elif action == 'exit':
            break


#coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
main_options(CoffeeMachine(400, 540, 120, 9, 550))