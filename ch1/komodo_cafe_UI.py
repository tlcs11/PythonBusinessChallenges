from komodo_cafe import Item, Menu
class Menu_UI:                                                #n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    def __init__(self):
        self.menu = Menu()

    def display_menu(self):
        print(
"""
Komodo Menu:
1. Add a menu item
2. Delete a menu item
3. Display the menu
4. Exit
"""
        )

    def run(self):
        while True:
            self.display_menu()
            choice = input("What would you like to do today:  ")
            if choice == "1":
                self.add_to_list()
            elif choice == "2":
                self.delete_from_list()
            elif choice == "3":
                self.show_list()
            elif choice == "4":
                exit()
            else:
                print("Try again invalid choice.")

    def show_list(self):
        menu_list = self.menu.get_menu()
        if menu_list:
            for item in menu_list:
                print(item)

    def add_to_list(self):
        order = input("What is the order #: ")
        name = input("Name of food: ")
        descr = input("Desc of food: ")
        ingredients = input("Ingredients in food: ")
        price = input("Price of food: ")
        self.menu.add_item(order, name, descr, ingredients, price)
        print("The item has been added to the menu.")

    def delete_from_list(self):
        self.show_list()
        message = input("Item name you like to delete: ")
        self.menu.delete_item(message)                                               #this is the path to the method
        print("The item has been deleted from the menu.")

if __name__ == "__main__":
    menu_ui = Menu_UI()
    menu_ui.run()


