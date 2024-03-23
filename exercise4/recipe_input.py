import pickle

def take_recipe(name='name', cooking_time='cooking_time', ingredients='ingredients', difficulty='difficulty'):
    name = input ("Name of recipe: ")
    cooking_time = int(input("How many minutes does it take to cook? "))
    ingredients = input("Please list the ingredients: ")
    recipe = {
        "name": name, 
        "cooking_time": cooking_time, 
        "ingredients": ingredients.split(', '),
        "difficulty": difficulty
    }
    return recipe

def calc_difficulty(cooking_time, ingredients, difficulty):
    if cooking_time < 10 and ingredients < 4:
        difficulty = 'Easy'
    elif cooking_time < 10 and ingredients >=4:
        difficulty = 'Medium'
    elif cooking_time >= 10 and ingredients < 4:
        difficulty = 'Intermediate'
    elif cooking_time >= 10 and ingredients >= 4:
        difficulty = 'Hard'
        return difficulty
    
#data is initialized
data = {'recipes_list': [], 'all_ingredients': []}
#user enters a filename
filename = input('Please enter the name of the file that contains your recipe data: ')
#the filename the user entered is used to load contents through the pickle module in a variable called 'data'
   
try:
    with open(filename, 'rb') as my_file:
        data = pickle.load(my_file)
        print('File loaded successfully')
except FileNotFoundError: 
    print('File not found.')
except:
    print('Oops, we have stumbled upon some undexpected error.')
else:
    my_file.close()
finally: 
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']
    print('List of Recipes: ')
    for recipe in recipes_list:
        print(recipe)
    print('List of All Ingredients: ')
    for ingredient in all_ingredients:
        print(ingredient)

n = int(input('How many recipes would you like to enter?'))
for i in range(n):
    recipe = take_recipe()
    recipes_list.append(recipe)
    #add ingredients from current recipe to all_ingredients if they're not already there
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
#dictionary to hold all updated recipes and ingredients
    data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}
#saving data to file
with open(filename, 'wb') as filename:
    pickle.dump(data, filename)


 
 
