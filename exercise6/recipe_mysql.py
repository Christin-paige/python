import mysql.connector

conn = mysql.connector.connect(host="localhost", user="cf-python", passwd="password")

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database3")
cursor.execute("USE task_database3")
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Recipes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,  
    difficulty VARCHAR(20)
)"""
)

cursor.execute("ALTER TABLE Recipes AUTO_INCREMENT = 1")

# display main menu to user
def main_menu(conn, cursor):
    choice = ""
    while True:
        print("Main Menu")
        print("=============================")
        print("Please choose an option from the menu")
        print("1. Create a Recipe")
        print("2. Search for an Ingredient")
        print("3. Update an Existing Recipe")
        print("4. Delete a Recipe")
        print("5. View all Recipes")
        print("Type 'quit' to exit the program")

        choice = input("Your choice: ")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            view_all_recipes(conn, cursor)
        else:
            return


def create_recipe(conn, cursor):
    name = input("Name of recipe: ")
    cooking_time = int(input("Time it takes to cook in minutes: "))
    ingredients = input("Please list the ingredients in the recipe: ").split(",")
    ingredients = ", ".join(ingredients)
    difficulty = calculate_difficulty(cooking_time, len(ingredients)) 

    
    sql = "INSERT INTO Recipes(name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    val = (name, ingredients, cooking_time, difficulty)
    cursor.execute(sql, val)
    conn.commit()
    print("Successfully saved recipe to database")


def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and ingredients < 4:
        difficulty = "Easy "
    if cooking_time < 10 and ingredients >= 4:
        difficulty = "Medium "
    if cooking_time >= 10 and ingredients < 4:
        difficulty = "Intermediate "
    if cooking_time >= 10 and ingredients >= 4:
       difficulty = "Hard "
    return difficulty
  


def search_recipe(conn, cursor):
    # retrieving ingredients from recipes table
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    # taking ingredients from results and removing duplicates
    all_ingredients = set()
    for row in results:
        ingredient = row[0]
        # splitting string into individual ingredients and adding them to the list
        ingredients_list = ingredient.split(",")
        all_ingredients.update(ingredients_list)

        # display ingredients
    print("All ingredients in recipes: ")
    for index, ingredient in enumerate(all_ingredients, start=1):
        print(f"{index}. {ingredient}")

    ingredient_choice = int(
        input("Enter the number corresponding to the ingredient you want to search:")
    )
    if ingredient_choice < 1 or ingredient_choice > len(all_ingredients):
        print("Must choose a number from list")
   
    search_ingredient = list(all_ingredients)[ingredient_choice - 1]
    query = "SELECT * FROM Recipes WHERE ingredients LIKE '%" + search_ingredient + "%'"
    cursor.execute(query)

    # fetch results
    search_results = cursor.fetchall()
    print(f"Recipes containing {search_ingredient}:")
    for row in search_results:
       print(row[1])

def update_recipe(conn, cursor):
    # fetching all recipes from database
    cursor.execute("SELECT id, name, ingredients, cooking_time, difficulty FROM Recipes")
    results = cursor.fetchall()
    results = [list(recipe) for recipe in results]  # Convert tuples to lists
    # display recipes to the user
    print("All recipes in database: ")
    for recipe in enumerate(results, start=1):
        print(f"{recipe[1]}")
        # asking to user to choose the recipe by it's index
    recipe_choice = int(
        input("Choose the number of the recipe you would like to update: ")
    )
    if recipe_choice < 1 or recipe_choice > len(results):
        print("Must choose a number from list")
        return
    # get selected recipe
    selected_recipe = results[recipe_choice - 1]
    recipe_id = selected_recipe[0]
    print(f"Selected Recipe: {selected_recipe}")
   
    # asking user which column they want to update
    column_choice = input(
        "Enter the name of the column you would like to update; name, ingredients, cooking_time: "
    )
    updated_value = input("Please enter the new value: ")

    if column_choice == "name":
        selected_recipe[1] = updated_value  # Update name in selected_recipe
    elif column_choice == "ingredients":
        updated_ingredients = selected_recipe[2] + ", " + updated_value
        selected_recipe[2] = updated_ingredients   # Update ingredients in selected_recipe
    elif column_choice == "cooking_time":
        selected_recipe[3] = int(updated_value)  # Update cooking time
        selected_recipe[4] = calculate_difficulty(selected_recipe[3], len(selected_recipe[2].split(", ")))  # Update difficulty
    else:
        print("Invalid choice")
        return update_recipe
    #execute the update queries
    update_query = f"UPDATE Recipes SET id = '{selected_recipe[0]}', name = '{selected_recipe[1]}', ingredients = '{selected_recipe[2]}', cooking_time = '{selected_recipe[3]}', difficulty = '{selected_recipe[4]}' WHERE id = {recipe_id}"

    #cursor.execute(update_query)update_query = f"UPDATE Recipes SET ... WHERE id = {recipe_id}"
    cursor.execute(update_query)
    conn.commit()
    print("Recipe update successful!")
    return update_recipe
  

def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
   
    print("All Recipes")
    print("=====================")
    for index, recipe in enumerate(results, start=1):
        print(f"{recipe[1]}")
    
      #asking the user to choose the recipe by it's index
    recipe_id_delete= input("Enter the name of the recipe you would like to delete: ")
 
    # row to be deleted is identified by the recipe_id that the user specifies
    #delete_query = "DELETE FROM Recipes WHERE id = (%s)"
    cursor.execute("DELETE FROM Recipes WHERE name = (%s)", 
                   (recipe_id_delete, ))
    conn.commit()
    print("Recipe deleted!")
   
def view_all_recipes(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    print("All Recipes")
    print("=======================")
    for row in results:
        print("ID:", row[0])
        print("Name: ", row[1])
        print("Ingredients: ", row[2])
        print("Cooking Time: " , row[3])
        print("Difficulty: ", row[4])
        print()
    conn.commit

main_menu(conn, cursor)
cursor.close()
conn.close()
