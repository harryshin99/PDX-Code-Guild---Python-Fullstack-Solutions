import requests
import json
import string
import random
import time

pokemon_url = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151'
response = requests.get(pokemon_url)
pokemon_data = json.loads(response.text)
pokemon= pokemon_data['results']

# print(pokemon)

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

# for index in range(len(pokemon_red)):
#     print(pokemon_red[index])
# for index in range(len(pokemon_stats)):
# for key, value in pokemon_stats.items():
#     print(key, value)

# pp = pprint.PrettyPrinter(depth=4)
# pp.pprint(pokemon_stats)

# choice = 'charmander'

# if choice in pokemon_stats:
#     print(choice)
#     print(f"weight: {pokemon_stats[choice]['weight']}")
#     print(f"type: {pokemon_stats[choice]['type']}")
#     print(f"ability: {pokemon_stats[choice]['ability']}")
bag = {
    'ultra-ball': 0,
    'master-ball': 10
}

user_name = 'Harry'
pokedex = []

while True:
    wild_pokemon = random.choice(pokemon_red)

    print(f"\nA wild {wild_pokemon} has appeared!")

    catch = input("\nDo you want to catch this Pokemon? ").lower()

    if catch in ['y', 'yeah', 'yes', 'ok', 'okay', 'sure', 'k']:
        while True:
            while True:
                for key, value in bag.items():
                    print(f"\nItem: {key} Quantity: {value}")
                
                use_item = input("\nSelect a Pokeball to throw: ")
                
                if use_item in bag and bag[use_item] > 0:
                    break
                elif use_item in bag and bag[use_item] < 1:
                    print(f"\nYou do not have anymore {use_item}s. Choose another item or back to the menu to purchase more items.")
                else:
                    print("\nPlease select an item from your bag.")


            bag[use_item] -= 1

            print(f"\n{user_name} used {use_item}!")
            time.sleep(1)
            print('...')
            time.sleep(1)
            print('...')
            time.sleep(1)
            print('...')
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
                print(f"{use_item} failed!")
                try_again = input("Do you want to throw another Pokeball? ").lower()
                use_item = ""
                if try_again in ['no', 'n', 'quit', 'done']:
                    break
        
    catch_more = input("\nDo you want to catch another Pokemon? ")
    if catch_more in ['no', 'n', 'quit', 'done']:
        break