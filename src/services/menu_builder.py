import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData


DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def __get_ingredients(self, recipe: dict) -> list:
        return [ingredient for ingredient in recipe]

    def __get_restrictions(self, recipe: dict[dict]) -> list:
        return list(
            set(
                restriction
                for ingredient in recipe
                for restriction in ingredient.restrictions
            )
        )

    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        items = self.menu_data.dishes
        dishes = [
            {
                "dish_name": dish.name,
                "price": dish.price,
                "ingredients": self.__get_ingredients(dish.recipe),
                "restrictions": self.__get_restrictions(dish.recipe),
            }
            for dish in items
            if (
                restriction not in set(self.__get_restrictions(dish.recipe))
                and self.inventory.check_recipe_availability(dish.recipe)
            )
        ]

        return pd.DataFrame(dishes)