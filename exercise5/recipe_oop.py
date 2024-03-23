class Recipe(object):
    all_ingredients = []

    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = None
       
    def calculate_difficulty(self):
       
        if self.cooking_time < 10 and len(self.ingredients) <4:
            self.difficulty = 'Easy'
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = 'Medium'
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = 'Intermediate'
        else:
            self.difficulty = 'Hard'

   
#getter and setter methods for name and cooking time
    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time
    
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

#method to add ingredients to ingredients list 
    def add_ingredients(self, ingredients):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)

#getter method to return list of ingredients
    def get_ingredients(self):
        return self.ingredients
    
#takes calculate_difficulty method from earlier and determines difficulty
    def get_difficulty(self):
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty
  

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients
    
#goes through ingredients and adds an ingredient if not in list
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    def __str__(self):
        output = f'Recipe Name: ' + str(self.name) + ' Ingredients: ' + str(self.ingredients) + ' Difficulty: ' + str(self.get_difficulty())
        return output
    

#method to find recipes that contain a specific ingredient
def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            return recipe

tea = Recipe('Tea', 5)
tea.add_ingredients(['Tea', 'Water', 'Sugar'])


coffee = Recipe('Coffee', 5)
coffee.add_ingredients(['Coffee Powder', 'Sugar', 'Water'])


cake = Recipe('Cake', 50)
cake.add_ingredients(['Sugar', 'Butter', 'Eggs', 'Vanilla Essence', 'Flour', 'Baking Powder', 'Milk'])


banana_smoothie = Recipe('Banana Smoothie', 5)
banana_smoothie.add_ingredients(['Bananas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice Cubes'])


recipes_list = [tea, coffee, cake, banana_smoothie]

for recipe in recipes_list:
   print(recipe)

for ingredient in ['Water', 'Sugar', 'Bananas']:
    print(recipe_search(recipes_list, ingredient))








