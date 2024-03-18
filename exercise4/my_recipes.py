import pickle
data = {
    "recipes_list": [
        {
            "name": 'Granola',
            "cooking_time": '10 minutes',
            "ingredients": 'oats, maple syrup, almond butter'.split(', ')  # Split ingredients into a list
        }
    ],
    "all_ingredients": ['oats', 'maple syrup', 'almond butter']  # List of all ingredients
}

with open('my_recipes.bin', 'wb') as my_file:
    pickle.dump(data, my_file)
    my_file.close()