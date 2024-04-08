import random
import time
import sys
from classes import Hero, Warrior, Monster, Archer, Mage


def main():
    while True:
        try:
            slow_print("******** Welcome to Arithmetic Ace! ********")
            slow_print("Choose which basic operation would you like to train! ")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Random")
            print("6. Mini Game")
            print("7. Exit")
            user_input = input("What is your choice (1-7)?: ")
            if user_input == '1':
                slow_print("You have selected Addition")
                set_size = set_size_chooser()
                question_generator('Addition', set_size)
                break
                
            elif user_input == '2':
                slow_print("You have selected Subtraction")
                set_size = set_size_chooser()
                question_generator('Subtraction', set_size)
                break
               
            elif user_input == '3':
                slow_print("You have selected Multiplication")
                set_size = set_size_chooser()
                question_generator('Multiplication', set_size)
                break
                
            elif user_input == '4':
                slow_print("You have selected Division")
                set_size = set_size_chooser()
                question_generator('Division', set_size)
                break

            elif user_input == '5':
                slow_print("You have selected Random")
                set_size = set_size_chooser()
                question_generator('Random', set_size)
                break
                
            elif user_input =='6':
                main_interface()
                break
            elif user_input =='7':
                sys.exit("Exiting program...")
            else:print("Invalid Input. Please try again.")
                
        except ValueError:
            print("Invalid input")

def set_size_chooser():
    while True:
        try:
            slow_print("****** Choose which Set size you prefer ******")
            slow_print(" 1. 5 Question set \n 2. 10 Question set")
            user_input = input("Select questions per set: ")

            if user_input== '1':
                set_size_chosen = 5
                break
            elif user_input == '2':
                set_size_chosen = 10
                break
            else:
                print("Invalid Input. Please try again")

        except ValueError:
            print("Invalid input. Please try again")

    return set_size_chosen

def question_generator(operation, set_size):
    
    #initialize variables
    total_questions = set_size
    time_limit = 10
    correct_marks = 0
    wrong_marks = 0
    x = 0

    while x < total_questions:
        x += 1
        try:
            start_time = time.time()
            number1 = random.randint(50, 100)
            number2 = random.randint(1, 50)

            if operation == 'Addition':
                correct_answer = add(number1, number2,)
                operator = '+'

            elif operation == 'Subtraction':
                correct_answer = subtract(number1, number2)
                operator = '-'

            elif operation == 'Multiplication':

                number1 = random.randint(1, 12)
                number2 = random.randint(6, 12)
                correct_answer = multiply(number1, number2)
                operator = '*'

            elif operation == 'Division':
                while True: 
                    number1 = random.randint(50, 100)
                    number2 = random.randint(1, 50)
                    if number1 % number2 != 0:
                       continue
                    else:
                        correct_answer = divide(number1, number2)
                        operator = '/'
                        
                        break
            else:
                if operation == 'Random':
                    operator = random.choice(['+', '-', '*', '/'])

                    if operator == '+':
                        correct_answer = add(number1, number2)

                    elif operator == '-':
                        correct_answer = subtract(number1, number2)

                    elif operator == '*':
                            number1 = random.randint(1, 12)
                            number2 = random.randint(6, 12)

                            correct_answer = multiply(number1, number2)

                    elif operator == '/':
                        while True: 
                            number1 = random.randint(50, 100)
                            number2 = random.randint(1, 50)
                            if number1 % number2 != 0:
                                continue
                            else:
                                correct_answer = divide(number1, number2)
                                break

            slow_print(f"What is {number1} {operator} {number2} ?")
            user_answer = (input("Enter your answer: "))

            end_time = time.time()
            elapsed_time = end_time - start_time

            # Checking if the answer is correct

            if elapsed_time < time_limit:
                
                #user_answer needs to be a string for this check to work    
                if not user_answer:
                    wrong_marks+=1
                    slow_print(f"{correct_answer} is the correct answer")
                # Turned user answer into an integer for comparison with the returned correct answer 
                elif int(user_answer) == correct_answer:
                    print("Correct!")
                    correct_marks += 1

                else:
                    print("Wrong answer!")
                    wrong_marks += 1
                    slow_print(f"{correct_answer} is the correct answer")

            else:
                slow_print("Your time is up! your answer is counted towards the wrong marks!")
                slow_print(f"{correct_answer} is the correct answer")
                wrong_marks +=1

        except ValueError:
            print("Invalid Input Please try again.")
        

    print(f"Correct answers: {correct_marks} Wrong answers: {wrong_marks}  ")
    
    # Prevents pop-up when function question generator is called in the arithmetic mini-game
    if set_size == 1:
        pass

    else:
        print("")
        slow_print("Return to main menu or run again?: ")
        choice = input("1. Return to main menu \n2. Run again \nEnter your choice(1-2): \n ")

        if choice =='1':
            main()
        elif choice =='2':
            question_generator(operation, set_size)
        else:
            print("Invalid Input.")
            slow_print("Returnig to main menu...")
            main()

    return wrong_marks, correct_marks

def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

def main_interface():
     while True:
        try:
            slow_print("******** Welcome to the Arithmetic Ace RPG mini-game! ********")
            slow_print("Available classes:")
            print("\t1. Warrior")
            print("\t2. Mage")
            print("\t3. Archer")
            print("\t4. Exit to main menu")

            user_choice = input("Which class would you like to play?(1-4): ")

            if user_choice == '1':
                slow_print("You have chosen Warrior...")
                slow_print("Warriors are frontline combatants known for their brute strength and resilience. \n Attributes:")
                print("\tStrength: High")
                print("\tDexterity: Moderate")
                print("\tIntelligence: Low")
                print("\tHP: High")
                confirm_choice()
                character_maker(user_choice)
                break

            elif user_choice =='2':
                slow_print("You have chosen Mage...")
                slow_print("Mages are spellcasters who harness the power of magic to manipulate the elements and cast devastating spells. \n Attributes: ")
                print("\tStrength: Low")
                print("\tDexterity: Moderate")
                print("\tIntelligence: High")
                print("\tHP: High")
                confirm_choice()
                character_maker(user_choice)
                break

            elif user_choice =='3':
                slow_print("You have chosen Archer...")
                slow_print("Archer is a skilled marksman proficient in ranged combat.  \n Attributes: ")
                print("\tStrength: Moderate")
                print("\tDexterity: High")
                print("\tIntelligence: Moderate")
                print("\tHP: High")
                confirm_choice()
                character_maker(user_choice)
                break

            elif user_choice =='4':
                main()
                break

            else:
                print("Invalid input. Please try again.")
                continue
        except ValueError:
            print("Invalid Input")

def confirm_choice():
    while True:
        try:
            print("Are you sure about your class selection? ")
            choice = input("Yes or No?: ").upper().strip()
            if choice =='YES':
                break
            elif choice =='NO':
                main_interface()
                break
            else:
                slow_print("Invalid Input. Please try again !!!")
        except ValueError:
            print("Invalid Input. Please try again.")

def character_maker(user_choice):
    while True:
        try:
            character_name = str(input("Enter your name: "))
            if user_choice == '1':
                player = Warrior(character_name)
                arithmetic_game(player, user_choice)
                break

            if user_choice == '2':
                player = Mage(character_name)
                arithmetic_game(player, user_choice)
                break

            if user_choice == '3':
                player = Archer(character_name)
                arithmetic_game(player, user_choice)
                break
            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid Input. Please try again.")

def arithmetic_game(player, user_choice):

    #Randomly generate monsters to be encountered by the player
    monsters_to_encounter = random.randint(2, 5)
    x = 0
    
    #Initialize player Inventory
    user_info = {'Inventory': {'HP POTION' : 5, 'MONSTER LOOT': 0}, 'Gold': 0}
    user_inventory[player] = user_info

    print(42*"*")
    slow_print(f"Welcome to the battlefield {player.name}! Here your arithmetic skills shall be put to the test!")
    slow_print("Before you go, take these HP potions!")
    slow_print("I>>>> Prepare for battle!!! <<<<I")
    print(42*"*")
    print("")

    while x < monsters_to_encounter:
        monster = Monster()
        print("")
        print(42*"*")
        slow_print(f"\tA wild {monster.name} has appeared!")
        print(42*"*")
        print("")

        x += 1
        while monster.hp >= 0:
            try:

                print("")
                print(42*"*")
                slow_print("\t\tPlayer's turn!")
                print(42*"*")
                print("")

                player_actions = input("What would you do? \n \t1. Attack \n \t2. Evade (Based on player stats) \n \t3. Cast Skill \n \t4. Open Inventory\n\nEnter action here(1-4): ")

                if not player_actions:
                    print("Please enter a number between 1-4.")
                    continue
                elif player_actions == '1':
                    pass
                elif player_actions =='2':
                    pass
                elif player_actions =='3':
                    pass
                elif player_actions =='4':
                    display_player_inventory(player, user_choice)
                    continue
                else:
                    slow_print("Invalid input. Please try again.")
                    continue
                
                slow_print("Quick! Solve the arithmetic problem to perfrom action!")
                
                #Initialize Variables
                correct_marks_total = 0
                wrong_marks_total = 0

                # Call the question generator function and catch the return values that will be used to evaluate if the user action succeeds or not
                
                wrong_marks, correct_marks = question_generator('Random', set_size=1)
                correct_marks_total = correct_marks
                wrong_marks_total = wrong_marks

                #Evaluate the user answer by tallying the correct marks and wrong marks
                if correct_marks_total > wrong_marks_total:

                    if player_actions == '1':
                            player.hero_attack(monster)
                    elif player_actions == '2':
                            player.hero_evade(monster)
                    elif player_actions == '3':
                            player.hero_cast_skill(monster)
                    elif player_actions == '4':
                        display_player_inventory(player)
                    else:
                        print("Invalid Choice. Please try again!")
                
                else:
                    print("") 
                    slow_print("****** Action Failed!!! ******")
                    print("")

                # Pause before ending player turn
                turn = input("End of turn (press Enter to continue)")
                if not turn:
                    pass

                else:
                    pass
                 
                #Check if player is slain

                if player.hp <= 0:
                    print(f"You have been slained by {monster.name}")
                    slow_print("Returning to main menu...")
                    main()
                    break

                #Checks if monster is slain
                if monster.hp <= 0:
                    gold = random.randint(2, 10)
                    Loot = monster_item_drops(monster)
                    print("")
                    slow_print(f"The monster named {monster.name} has been slained dropping {gold} pieces of gold and {Loot} pieces of Monster Loot.")
                    print("")
                    print(f"Player HP : {int(player.hp)} Monster HP:{0} ")
                
                    #Update User Inventory
                    
                    user_inventory[player]['Gold'] += gold
                    user_inventory[player]['Inventory']['MONSTER LOOT'] = Loot

                    merchant_shop(player)

                else:
                    # If not slain proceed to monster's turn
                    print("")
                    slow_print("******** Monster's turn ********")
                    print("")
                    # Prevents monster from attacking two times in a sinlge turn since in the class method hero_evade() the player takes damage from the mosnter if the check condition for evasion is not met 
                    #It is due to the fact that player evasion is based on stats and not the tally of correct or wrong marks
                    if player_actions == '2':
                        pass
                    else:
                        monster.monster_attack(player)
                    print("")
                    slow_print(f"Player HP : {int(player.hp)} Monster HP:{int(monster.hp)} ") 
                    print("")
            except ValueError:
                print("Invalid input. Please try again.")
    else:
        print("")
        print(f"Battle Over!.{player.name} you have slained {monsters_to_encounter} monsters!")
        print("Well Done Math Warrior!")
        print("")
        main()

user_inventory = {'Player' : {'Inventory' : {}, 'Gold': 0 } }

def take_inventory(player):

    while True:
        try:
            print("")
            item = input("Select item from inventory(Press enter to return to user menu): ").upper()

            if not item:
                break

            if item in user_inventory[player]['Inventory']:
                print(f"The item {item} has been successfully selected")

                if item == 'HP POTION':

                    print("Item is consumable. Consume item to replenish HP?: ")
                    choice = input("Yes or No: ").upper().strip()

                    if choice == 'YES':
                        if player.hp >= 100:
                            slow_print("Player HP is full...")
                            break
                        elif user_inventory[player]['Inventory']['HP POTION'] <= 0:
                            slow_print("Insufficeint HP Potions")
                            break
                        else:
                            #Check if player hp is greater than maximum allowed
                            player.hp += 25
                            if player.hp > 100:
                                player.hp = 100
                        
                            #Update user inventory
                            user_inventory[player]['Inventory']['HP POTION'] -= 1

                        slow_print(f"{player.name}'s health has been restored by 25 points !!!")
                        break

                    elif choice == 'NO':
                        pass

                    elif not choice:
                        continue

                    else:
                        print("Invalid Input. Please enter Yes or No only!")
                        continue
                else:
                    print("Item is not consumable. Consider selling this to any merchants for Gold.")
                    continue
            else:
                slow_print(f"{item} does not exist")
                continue
          
        except ValueError:
            print("Invalid Input. Please try again !!!")

def display_player_inventory(player, user_choice ):

    if not user_inventory.get(player, {}).get('Inventory'):
        print("Inventory is empty")
    
    else:
        print(42*"*")

        print(f"{player.name}'s Inventory:")
        for key, value in user_inventory[player]['Inventory'].items():
            slow_print(f"Item: {key}, Quantity: {value}")

        slow_print(f"Gold: {user_inventory[player]['Gold']}")

        if user_choice =='1':
            print("Class: Warrior")
        if user_choice =='2':
            print("Class: Mage")
        if user_choice =='3':
            print("Class: Archer")
        print(42*"*")

        take_inventory(player)

def monster_item_drops(monster):
    if monster =='Goblin' or 'Orc' or 'Zombie':
        quantity = random.randint(2, 5)    
        return quantity
    else:
        print("Monster encountered not in Monster Classes !!!")
        slow_print("Terminating program...")
        sys.exit()

merchan_ware = {'HP Potion': {'Cost': 5, 'Quantity': 50}, 'Gold' : 100 }

def merchant_shop(player):

    print(42*"*")
    slow_print("Would you like to stop by a merchant?")
    print(42*"*")

    while True:
        try:
            choice = input("Yes or No: ").upper().strip()
                
            if not choice:
                break

            if choice =='YES':
                merchant_shop_choice(player)
                break
            else:
                break
            

        except ValueError:
            print("Invalid Input. Please try again")

def merchant_shop_choice(player):
     while True:
        try:
            print("")
            print("***** Actions ***** \n 1. Buy HP potions \n 2. Sell Monster Loot")
            print("******** Press ENTER to close shop ********")
            print("")
            player_action = input(" 1 or 2: ")

            if player_action == '1':
                buy_potion(player)
                break
            elif player_action =='2':
                sell_loot(player)
                break
            elif not player_action:
                break
            else:
                print("Invalid Input")
                continue
    
        except ValueError:
            print("Invalid Input. Please try again.")


def buy_potion(player):
    while True:
        try:
            quantity_str = (input("How many would you like to buy?: "))

            if not quantity_str:
                merchant_shop_choice(player)
                break

            quantity = int(quantity_str)
                
            if quantity > merchan_ware['HP Potion']['Quantity']:
                slow_print("Insufficient stocks")
                merchant_shop_choice(player)
                break

            total_cost = quantity * merchan_ware["HP Potion"]['Cost']

            if user_inventory[player]['Gold'] < total_cost:
                slow_print("Insufficient Balance")
                merchant_shop_choice(player)
                break

            if quantity <= 0:
                print("Invalid Quantity")
                merchant_shop_choice(player)
                break

            user_inventory[player]['Inventory']['HP POTION'] += quantity
            user_inventory[player]['Gold'] -= total_cost
            merchan_ware["HP Potion"]['Quantity'] -=quantity
            merchan_ware['Gold'] += total_cost

            print(f"Successfully bought {quantity} pieces of Hp postions")
            slow_print("Do another transacton with merchant?")

            action = input("1. Yes \n2. No \n Enter choice here: ").upper().strip()
            if action == 'YES':
                merchant_shop_choice(player)
                break
            elif action =='NO':
                break
            else:
                merchant_shop_choice(player)
    
        except ValueError:
            print("Invalid Input. Please try again.")

def sell_loot(player):
    while True:
        try:
           
            quantity_str = (input("How many would you like to sell?: "))

            if not quantity_str:
                merchant_shop_choice(player)
                break
         
            quantity = int(quantity_str)

            if quantity > user_inventory[player]['Inventory']['MONSTER LOOT']:
                print("Quantity exceeds what is in user inventory!")
                merchant_shop_choice(player)
                break
            
            profit = quantity * 2

            if profit > merchan_ware["Gold"]:
                print("Merchant has insufficient money. Consider lowering the amount of Loot to sell")
                merchant_shop_choice(player)
                break

            user_inventory[player]['Gold'] += profit
            user_inventory[player]['Inventory']['MONSTER LOOT'] -= quantity
            slow_print(f"Successfully sold Monster Loot for {profit} pieces of Gold")

            slow_print("Do another transacton with merchant?")
            action = input("1. Yes \n2. No \n Enter choice here: ").upper().strip()

            if action == 'YES':
                merchant_shop_choice(player)
                break
            elif action =='NO':
                break
            else:
                merchant_shop_choice(player)

        except ValueError:
            print("Invalid Input, Please try again.")

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
main()
