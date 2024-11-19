# Step 1: Import the necessary libraries
import pandas as pd

# Step 2: Create a data dictionary
data = {
    "evolution": ["Ivysaur", "Charmeleon", "Wartortle", "Metapod"],
    "hp": [45, 39, 44, 45],
    "name": ["Bulbasaur", "Charmander", "Squirtle", "Caterpie"],
    "pokedex": ["yes", "no", "yes", "no"],
    "type": ["grass", "fire", "water", "bug"]
}

# Step 3: Assign it to a variable called pokemon
pokemon = pd.DataFrame(data)

# Step 4: Place the order of the columns as name, type, hp, evolution, pokedex
pokemon = pokemon[["name", "type", "hp", "evolution", "pokedex"]]

# Step 5: Add another column called place and insert what you have in mind
pokemon["place"] = ["forest", "mountain", "sea", "forest"]

# Step 6: Present the type of each column
print("Column types:")
print(pokemon.dtypes)

# Step 7: Display the rows where hp is greater than 44
print("\nPokemon with hp greater than 44:")
print(pokemon[pokemon["hp"] > 44])
