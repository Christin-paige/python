#pickle stores data into a binary file
import pickle
#pickle.load() reads the binary file
with open('my_recipes.bin', 'rb') as my_file:
   recipe = pickle.load(my_file)
#output in a readable format
print('Recipe Name: ' + recipe['ingredient_name'])
#use .join to display a list within a dictionary
print('Ingredients: ', ','.join(recipe['ingredients']))
print('Cooking Time: ' + recipe['cooking_time'])
print('Difficulty: ' + recipe['difficulty'])