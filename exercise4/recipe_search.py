import pickle

def display_recipe(recipe):
    print('Recipe Name: ' + recipe['name'])
    print('Cooking Time: ' + recipe['cooking_time'])
    #used .join() to list ingredients within dictionary
    print('Ingredients: ', ','.join(recipe['ingredients']))
    print('Difficulty: ',  recipe['difficulty'])

#searches for an ingredient within the given list
def search_ingredient(data):
    available_ingredients = enumerate(data['all_ingredients'])
    numbered_list = list(available_ingredients)

#user picks a number that is used as the index to retrieve corresponding ingredient
    try:
        number = int(input("Pick a number from this list: "))
        ingredient_searched = numbered_list[number][1]
    except ValueError: 
            print('Warning, input may be incorrect')
    else: 
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
    #'f' at the beginning of print statement allows embedding within a string literal
                print(f"'{recipe['name']}' contains '{ingredient_searched}'")

try:
    user_input = input('What is the name of the file you wish to open? ')
    with open(user_input, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    print('File has not been found')
else:
    search_ingredient(data)