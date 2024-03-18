import pickle

with open('recipe_binary.bin', 'rb') as my_file:
   recipe = pickle.load(my_file)

print('Recipe Name: ' + recipe['ingredient_name'])
print('Ingredients: ', ','.join(recipe['ingredients']))
print('Cooking Time: ' + recipe['cooking_time'])
print('Difficulty: ' + recipe['difficulty'])