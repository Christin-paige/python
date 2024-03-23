#pickle stores data into a binary file
import pickle
#pickle.load() reads the binary file
with open('my_recipes.bin', 'rb') as my_file:
    recipe = pickle.load(my_file)
print('Recipe Name: ' + recipe['name'])
print('Cooking Time: ' + recipe['cooking_time'])
#used .join() to list ingredients within dictionary
print('Ingredients: ', ','.join(recipe['ingredients']))
print('Difficulty: ', + recipe['difficulty'])