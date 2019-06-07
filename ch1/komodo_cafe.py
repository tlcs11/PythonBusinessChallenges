class Item:
    def __init__(self, order, name, descr, ingredients, price):
        self.order = order
        self.name = name
        self.descr = descr
        self.ingredients = ingredients
        self.price = price

    def __repr__(self):
        return f"{self.name} {self.price}"


class Menu:
    def __init__(self):
        self.menu_list = []

    def add_item(self, order, name, descr, ingredients, price):        #
        new_item = Item(order, name, descr, ingredients, price)
        self.menu_list.append(new_item)

    def delete_item(self, name):
        for food in self.menu_list:
            if name == food.name:
                self.menu_list.remove(food)                

    def get_menu(self):
        return self.menu_list
