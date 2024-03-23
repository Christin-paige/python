recipes_list=[]
ingredients_list=[]

#name (str) stores name of recipe
#cooking_time(int)stores cooking time in minutes
#ingredients(list)list that stores ingredients,each of the string data type
#recipe(dictionary) stores name, cooking time, ingredients (already made in last exercise)


n = int(input("How many recipes would you like to enter? "))

def take_recipe(name='name', cooking_time='cooking_time', ingredients='ingredients', difficulty='difficulty', recipe='recipe'):
    #result = name + cooking_time + ingredients + recipe
    name = input ("Name of recipe: ")
    cooking_time = int(input("How many minutes does it take to cook? "))
    ingredients = input("Please list the ingredients: ")
    recipe = {
        "name": name, 
        "cooking_time": cooking_time, 
        "ingredients": ingredients.split(', ')
    }
    return recipe

for i in range(n):
        recipe = take_recipe()
        for ingredient in recipe['ingredients']:
            if ingredient not in ingredients_list:
                ingredients_list.append(ingredient)
        recipes_list.append(recipe)
    
            
for recipe in recipes_list:
    if int(recipe ['cooking_time']) < 10 and len(recipe['ingredients']) < 4:
        difficulty = 'easy'
    elif int(recipe ['cooking_time']) < 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'medium'
    elif int(recipe ['cooking_time']) >= 10 and len(recipe['ingredients']) < 4:
        difficulty = 'intermediate'
    elif int(recipe ['cooking_time']) >= 10 and len(recipe['ingredients']) >= 4:
        difficulty = 'hard'

    def get_all_ingredients(recipes):
         ingredients_list = []
         for recipe in recipes:
              ingredients_list.extend(recipe['ingredients'])
              ingredients_list.sort()
         return ingredients_list

    
    print("Recipe: ", recipe['name'])
    print("Cooking Time (min): ", recipe['cooking_time'])
    print("Ingredients: ")
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print("Difficulty level: " + difficulty)

  

ingredients_list = get_all_ingredients(recipes_list)
print("Ingredients Available Across All Recipes: ")
for ingredient in ingredients_list:
     
     print(ingredient)  
     
    
    
    
    
   

        









#for loop - run take_recipe() and store its return output (dictionary) in a variable called recipe
#nest another for loop that iterates through a recipe's ingredient list, where elements are picked out one-by-one as ingredient
#if chosen ingredient isn't present, add it to the list
#if ele in seq: (checks if an element is in sequence)


