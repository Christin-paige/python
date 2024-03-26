def create_recipe(conn, cursor):
    name = input("Name of recipe: ")
    cooking_time = int(input('Time it takes to cook in minutes: '))
    ingredients = input("Please list the ingredients in the recipe: ").split(',')
    ingredients = ', '.join(ingredients)
    difficulty = "difficulty"

    sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)'
    val = (name, ingredients, cooking_time, difficulty)
    cursor.execute(sql, val)
    conn.commit()
    print("Successfully saved recipe to database")



def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and ingredients < 4:
        difficulty = 'Easy'
    if cooking_time < 10 and ingredients >= 4:
        difficulty = "Medium"
    if cooking_time >= 10 and ingredients < 4:
        difficulty = "Intermediate"
    if cooking_time >= 10 and ingredients >= 4:
        difficulty = "Hard"
    print("Difficulty level: ", difficulty)
    return difficulty

def search_recipe(conn, cursor):
    return search_recipe(conn, cursor)

def update_recipe(conn, cursor):
    return update_recipe(conn, cursor)

def delete_recipe(conn, cursor):
    return delete_recipe(conn, cursor)

def main_menu(conn, cursor):
    return main_menu(conn, cursor)
   

while(choice != 'quit'):
    print("Please choose an option from the menu")
    print("1. Create a Recipe")
    print("2. Search for a Recipe")
    print("3. Update an Existing Recipe")
    print("4. Delete a Recipe")
    choice = input("Your choice: ")

    if choice == '1':
        create_recipe(conn, cursor)
    elif choice == '2':
        search_recipe()
    elif choice == '3':
        update_recipe()
    elif choice == '4':
        delete_recipe()
    else:
        choice == 'quit'

