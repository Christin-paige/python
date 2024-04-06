from sqlalchemy import create_engine, Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
#added +mysqlconnector to successfully connect to database
engine = create_engine(
    "mysql+mysqlconnector://cf-python:password@localhost/task_database"
)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return (
            "<Recipe ID: "
            + str(self.id)
            + "-"
            + self.name
            + "Difficulty: "
            + self.difficulty
            + ">"
        )

    def __str__(self):
        return (
            "Recipe Name: "
            + self.name
            + "\n"
            + "Ingredients: "
            + self.ingredients
            + "\n"
            + "Cooking Time: "
            + str(self.cooking_time)
            + "\n"
            + self.difficulty
        )

    print("Thank you", end="-")

    print("goodbye")

    def calculate_difficulty(self):

        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"


def return_ingredients_as_list(self):
    if not self.ingredients:
        return []
    else:
        return self.ingredients(", ")

Base.metadata.create_all(engine)


def create_recipe():
    name = input("Please enter the name of your recipe: ")
    ingredients = input("Enter ingredients separated by a comma: ")
    cooking_time = input("Time in minutes it takes to cook: ")
#ensuring recipe meets Recipe class requirements
    if len(name) > 50 or not name.isalnum:
        print("Name cannot exceed 50 characters.")
        return
    ingredients_list = ingredients.split(", ")

    recipe_entry = Recipe(
        name=name,
        ingredients=", ".join(ingredients_list),
        cooking_time=int(cooking_time),
    )
    recipe_entry.calculate_difficulty()

    session.add(recipe_entry)
    session.commit()
    print("recipe entered successfully")


def view_all_recipes():
    recipes_list = session.query(Recipe).all()
    if recipes_list is None:
        return None
    for recipe in recipes_list:
        print("====================")
        print("Recipe Name: ", recipe.name)
        print("Ingredients: ", recipe.ingredients)
        print("Cooking Time: ", recipe.cooking_time)
        print("Difficulty: ", recipe.difficulty)
        print("====================")
    session.commit()


def search_by_ingredients():
    ingredient_list = session.query(Recipe.ingredients).all()
    all_ingredients = set()
    for (ingredients_str,) in ingredient_list:
        all_ingredients.update(ingredients_str.split(", "))

    if not all_ingredients:
        print("There are no recipes in the database")
        return

    print("All ingredients in recipes: ")
    print("============================")
    for index, ingredient in enumerate(all_ingredients, 1):
        print(f"{index}. {ingredient}")

    ingredient_choice = int(
        input(
            "Please choose a number corresponding to the ingredients you would like to see: "
        )
    )
    if ingredient_choice < 1 or ingredient_choice > len(all_ingredients):
        print("Invalid choice. Must choose a number from list")
        return

    chosen_ingredient = list(all_ingredients)[ingredient_choice - 1]

    search_results = (
        session.query(Recipe)
        .filter(Recipe.ingredients.like(f"%{chosen_ingredient}%"))
        .all()
    )

    print(f"Recipes containing '{ingredient_choice}':")
    for recipe in search_results:
        print(recipe)


def edit_recipe():
    recipes_list = session.query(Recipe).all()

    if not recipes_list:
        print("There are no recipes in the database")
        return

    print("Available Recipes:")
    for index, recipe in enumerate(recipes_list, 1):
        print(f"{index}. {recipe.name}")

    user_choice = input(
        "Type the corresponding number next to the item you would like to edit: "
    )
    if not user_choice.isdigit():
        print("Invalid choice, please choose a number")
        return
    user_choice = int(user_choice)
    if user_choice < 1 or user_choice > len(recipes_list):
        print("Invalid choice, please choose a number from the list")
        return
    selected_recipe = recipes_list[user_choice - 1]
    selected_recipe = session.query(Recipe).filter_by(name=selected_recipe.name).first()

    print("1. Name: ", selected_recipe.name)
    print("2. Ingredients: ", selected_recipe.ingredients)
    print("3. Cooking Time: ", selected_recipe.cooking_time)

    edit_choice = input(
        "Choose the number corresponding to the item you would like to edit: "
    )

    if edit_choice == "1":
        new_name = input("Enter a new name: ")
        selected_recipe.name = new_name
    elif edit_choice == "2":
        new_ingredients = input("Enter the new ingredients: ")
        selected_recipe.ingredients = new_ingredients
    elif edit_choice == "3":
        new_cooking_time = input("Enter a new cooking time: ")
        selected_recipe.cooking_time = new_cooking_time
    else:
        return

    session.commit()
    print("Recipe edited successfully!")

def delete_recipe():
    recipes_list = session.query(Recipe.id, Recipe.name).all()
    if not recipes_list:
        print("There are no recipes in the database")

    print("Available Recipes: ")
    for index, recipe in enumerate(recipes_list, 1):
        print(f"{index}. {recipe.name}")

    user_choice = input(
        "Please enter the corresponding number of the recipe you would like to delete: "
    )
    if not user_choice.isdigit():
        print("Invalid choice. Please enter a number.")
        return
    user_choice = int(user_choice)
    if user_choice < 1 or user_choice > len(recipes_list):
        print("Invalid choice, please choose a number from the list.")
        return
    selected_recipe = recipes_list[user_choice - 1]

    selected_recipe = session.query(Recipe).filter_by(id=selected_recipe.id).first()
    confirm_delete = input(
        f"Are you sure you want to delete this recipe? '{selected_recipe.name}'? (yes/no): "
    )
    if confirm_delete == "yes":
        session.delete(selected_recipe)
        session.commit()
        print("Recipe deleted successfully")
    else:
        print("Deletion canceled.")


def main_menu():
    while True:
        print(
            """\***********************************************
* ██████   ██████            ███                *
*░░██████ ██████            ░░░                 *
* ░███░█████░███   ██████   ████  ████████      *
* ░███░░███ ░███  ░░░░░███ ░░███ ░░███░░███     *
* ░███ ░░░  ░███   ███████  ░███  ░███ ░███     *
* ░███      ░███  ███░░███  ░███  ░███ ░███     *
* █████     █████░░████████ █████ ████ █████    *
*░░░░░     ░░░░░  ░░░░░░░░ ░░░░░ ░░░░ ░░░░░     *
*                                               *
*                                               *
*                                               *
* ██████   ██████                               *
*░░██████ ██████                                *
* ░███░█████░███   ██████  ████████   █████ ████*
* ░███░░███ ░███  ███░░███░░███░░███ ░░███ ░███ *
* ░███ ░░░  ░███ ░███████  ░███ ░███  ░███ ░███ *
* ░███      ░███ ░███░░░   ░███ ░███  ░███ ░███ *
* █████     █████░░██████  ████ █████ ░░████████*
*░░░░░     ░░░░░  ░░░░░░  ░░░░ ░░░░░   ░░░░░░░░ *
************************************************* """
        )
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit a Recipe")
        print("5. Delete a recipe")
        print("6. Quit")

        choice = input("Enter your choice: ")
        print("--------------------")

        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

        session.commit()


main_menu()
