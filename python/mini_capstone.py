import requests
import json
import random
import time

pokeball_url = 'https://pokeapi.co/api/v2/item/?offset=0&limit=15'
response = requests.get(pokeball_url)
pokeball_data = json.loads(response.text)
pokeball = pokeball_data['results']

pokemon_url = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151'
response = requests.get(pokemon_url)
pokemon_data = json.loads(response.text)
pokemon= pokemon_data['results']

pokeball_cost = {}
pokeball_info = []
for index in range(len(pokeball)):
    item_url = pokeball[index]['url']
    item_response = requests.get(item_url)
    item_data = json.loads(item_response.text)
    pokeball_cost[item_data['name']] = item_data['cost']
    pokeball_info.append(f"{item_data['name']}: {item_data['effect_entries'][0]['short_effect']}")

pokemon_red = []
pokemon_stats = {}
for index in range(len(pokemon)):
    pokemon_url = pokemon[index]['url']
    pokemon_response = requests.get(pokemon_url)
    pokemon_data = json.loads(pokemon_response.text)
    pokemon_red.append(pokemon[index]['name'])
    pokemon_stats[pokemon[index]['name']] = {}
    pokemon_stats[pokemon[index]['name']]['weight'] = pokemon_data['weight']
    pokemon_stats[pokemon[index]['name']]['type'] = pokemon_data['types'][0]['type']['name']
    pokemon_stats[pokemon[index]['name']]['ability'] = pokemon_data['moves'][0]['move']['name']

balance = 10000
bag = {}
pokedex = []

user_name = input("Welcome to Pokemon Safari! What is your name? ")
print("\n******************************************************")

print("\n"f'Welcome {user_name}! Before you can enter the Safari park, you will need to purchase some Pokeballs.')

while True:
    choice = input(
    '\nEnter "menu" to purchase Pokeballs.'

    '\n\nEnter "info" to for more information on each type of Pokeball. '

    '\n\nEnter "bag" to view the contents of your bag. '

    '\n\nEnter "pokemon" to view the current list of Pokemon in the park. '
        'You can check your Poke-Dex for stats of the Pokemon you catch.'

    '\n\nEnter "pokedex" to view information on the Pokemon you\'ve caught. '

    '\n\nEnter "safari" to catch-em-all! '

    '\n\nEnter "done" to leave the Safari park. '

    '\n\nSelection: ').lower()

    print("\n******************************************************")

    if choice == 'done':
            print(f"\nThanks for visiting Pokemon Safari {user_name}. See you again soon!")
            break

    if choice not in ['menu', 'info', 'bag', 'pokemon', 'pokedex', 'safari', 'done']:
        print("\nPlease enter a valid selection.")
        choice = 'main'

    while True:
        if choice == 'main':
            break

        if choice == 'menu':

            print(f"""
                    Pokeball Menu
            Your starting balance is ${balance}.""" + "\n")

            for key, value in pokeball_cost.items():
                print(f"{key}  ${value}")

            buy_pokeball = input(
            "\nEnter 'main' to go back to the main menu.\n"
            "Enter 'info' for more information on each Pokeball.\n\n"

            "Which Pokeball would you like to buy? \n\n"

            "Selection: ").lower()
            print("\n******************************************************")

            if buy_pokeball == 'main':
                break

            elif buy_pokeball == 'info':
                choice = 'info'

            elif buy_pokeball in pokeball_cost:
                quantity = int(input(f"\nHow many {buy_pokeball}s would you like to purchase? "))
                cost = quantity * int(pokeball_cost[buy_pokeball])
                if cost > balance:
                    choice = input(f"\nYour cost of ${cost} exceeds your balance of ${balance}.\n"
                            "Please choose another pokeball/quantity or return to the main menu.\n"
                            "Enter any key to continue: ")
                    choice = 'menu'
                    print("\n******************************************************")
                elif cost <= balance:
                    balance -= cost
                    if buy_pokeball not in bag:
                        bag[buy_pokeball] = quantity
                    else:
                        bag[buy_pokeball] += quantity
                    print(f"You have added {quantity} {buy_pokeball}s to your bag.")
                    print(f"Your remaining balance is ${balance}.")
                    choice = input("\nWould you like to purchase more Pokeballs? ").lower()
                    if choice in ['y', 'yeah', 'yes', 'ok', 'okay', 'sure', 'k']:
                        choice = 'menu'
                        print("\n******************************************************")
                    else:
                        choice = 'main'
                        print("\n******************************************************")
            
            elif buy_pokeball not in pokeball_cost:
                choice = input("\nPlease enter a valid selection. Press any key to return to the menu: ")
                choice = 'menu'
                print("\n******************************************************")


        if choice == 'info':
            print("\n")
            for index in range(len(pokeball_info)):
                print(pokeball_info[index])
            choice = input("\nEnter any key when done: ")
            choice = "main"
            print("\n******************************************************")

        if choice == 'bag':
            if len(bag) == 0:
                print("\nYour bag is empty. Go to the menu to purchase items.")
            for key, value in bag.items():
                print(f"\nItem: {key} Quantity: {value}")
            choice = input("\nEnter any key when done: ")
            choice = "main"
            print("\n******************************************************")

        if choice == 'pokemon':
            print("\nThese are the current Pokemon roaming the park:\n")
            for index in range(len(pokemon_red)):
                print(pokemon_red[index])
            choice = input("\nEnter any key to return to the main menu: ")
            choice = 'main'
            print("\n******************************************************")

        if choice == 'pokedex':
            if len(pokedex) == 0:
                print("\nYour Poke-Dex is empty. Please catch some Pokemon to view their stats.")
                choice = input("\nEnter any key to return to the main menu: ")
                choice = 'main'
                print("\n******************************************************")
            elif len(pokedex) > 0:
                print(f"\nGreat job {user_name}! Here are the pokemon you've caught so far: ")
                while True:
                    print("\n")
                    for index in range(len(pokedex)):
                        print(pokedex[index])
                    see_pokemon = input("\nEnter the name of the Pokemon you'd like to view: ")
                    print("\n******************************************************")
                    if see_pokemon in pokemon_stats:
                        print(see_pokemon)
                        print(f"weight: {pokemon_stats[see_pokemon]['weight']}")
                        print(f"type: {pokemon_stats[see_pokemon]['type']}")
                        print(f"ability: {pokemon_stats[see_pokemon]['ability']}")
                        cont = input(f"\nWould you like to see another Pokemon? ").lower()
                        if cont in ['n', 'no', 'done', 'quit']:
                            print("\n******************************************************")
                            break
                    else:
                        print("\nYou have not caught this Pokemon yet. Please see your Poke-Dex.")
                        print("\n******************************************************")
                choice = input("\nEnter any key to return to the main menu: ")
                print("\n******************************************************")
                choice = 'main'

        if choice == 'safari':
            if len(bag) == 0:
                print("\nYou do not have any Pokeballs in your bag to catch Pokemon.")
                print("\nPlease visit the Safari Menu to purchase your items.")
                choice = input("\nEnter any key to continue: ")
                choice = 'main'
                print("\n******************************************************")
                break

            print("\nWelcome to the Safari Zone! You can begin catching wild Pokemon! Good luck!")

            while True:
                wild_pokemon = random.choice(pokemon_red)

                print(f"\nA wild {wild_pokemon} has appeared!")

                catch = input("\nDo you want to catch this Pokemon? ").lower()
                print("\n******************************************************")

                if catch in ['y', 'yeah', 'yes', 'ok', 'okay', 'sure', 'k']:
                    while True:
                        while True:
                            for key, value in bag.items():
                                print(f"\nItem: {key} Quantity: {value}")
                            
                            use_item = input("\nSelect a Pokeball to throw: ")
                            print("\n******************************************************")

                            
                            if use_item in bag and bag[use_item] > 0:
                                break
                            elif use_item in bag and bag[use_item] < 1:
                                print(f"\nYou do not have anymore {use_item}s. Choose another item or back to the menu to purchase more items.")
                                any_key = input("\nEnter any key to continue with your battle: ")
                                print("\n******************************************************")
                            else:
                                print("\nPlease select an item from your bag.")
                                any_key = input("\nEnter any key to continue with your battle: ")
                                print("\n******************************************************")

                        bag[use_item] -= 1

                        print(f"\n{user_name} used {use_item}!")
                        time.sleep(1)
                        print('\n...')
                        time.sleep(1)
                        print('\n...')
                        time.sleep(1)
                        print('\n...')
                        time.sleep(1)
                        if use_item == 'master-ball':
                            print(f"\nAlright! {wild_pokemon} was caught!")
                            pokedex.append(wild_pokemon)
                            break
                        elif random.randint(1,3) == random.randint(1,3):
                            print(f"\nAlright! {wild_pokemon} was caught!")
                            pokedex.append(wild_pokemon)
                            break
                        else:
                            print(f"\n{use_item} failed!")
                            try_again = input("\nDo you want to throw another Pokeball? ").lower()
                            use_item = ""
                            if try_again in ['no', 'n', 'quit', 'done']:
                                print("\n******************************************************")
                                break
                    
                catch_more = input("\nDo you want to catch another Pokemon? ")
                if catch_more in ['no', 'n', 'quit', 'done']:
                    print("\n******************************************************")
                    choice = 'main'
                    break