recipes_list=[]
ingredients_list=[]


#name (str) stores name of recipe
#cooking_time(int)stores cooking time in minutes
#ingredients(list)list that stores ingredients,each of the string data type
#recipe(dictionary) stores name, cooking time, ingredients (already made in last exercise)

def take_recipe(name, cooking_time, ingredients, recipe):
    result = name + cooking_time + ingredients + recipe
    print("The recipe is " + str(result))


name = str(input ("Name of recipe: "))
cooking_time = int(input("How many minutes does it take to cook? "))
ingredients = str(input("Please list the ingredients: "))
recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients}

#print("recipe: " + str(name))
#print("ingredients: " + str(ingredients))
#print("cooking time: " + str(cooking_time) + " min")
print(recipe)

n = int(input("How many recipes would you like to enter?"))
