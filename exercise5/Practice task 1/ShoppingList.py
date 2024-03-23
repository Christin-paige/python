class ShoppingList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.pet_store_list = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)


    def remove_item(self, item):
           try:
             self.shopping_list.remove(item)
           except:
                print('Item not found')

    def view_list(self):
        if self.shopping_list:
            print(f"{self.list_name}:")
            for item in self.shopping_list:
                print(item)
        else:
            print(f'{self.list_name} is empty.')
       
pet_store_list = ShoppingList('Pet Store Shopping List')
        
pet_store_list.add_item('dog food')
pet_store_list.add_item('frisbee')
pet_store_list.add_item('bowl')
pet_store_list.add_item('collars')
pet_store_list.add_item('flea collars')


pet_store_list.remove_item('flea collars')
pet_store_list.add_item('frisbee')

pet_store_list.view_list()

   




    
   
    