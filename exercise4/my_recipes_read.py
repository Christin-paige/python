import pickle

with open('my_recipes.bin', 'rb') as my_file:
    recipe = pickle.load(my_file)
#output in a readable format
print('Recipe Name: ' + recipe['name'])
#use .join to display a list within a dictionary
print('Ingredients: ', (recipe['ingredients']))
print('Cooking Time: ' + recipe['cooking_time'])
