import pandas as pd
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        for dish_name, dish_rows in (
            pd.read_csv(source_path).drop_duplicates().groupby("dish")
        ):
            ingredients = {}
            price = dish_rows["price"].iloc[0]
            dish_description = Dish(dish_name, price)
            for row in dish_rows.to_dict("records"):
                ingredient_name = row["ingredient"]
                if ingredient_name not in ingredients:
                    ingredients[ingredient_name] = Ingredient(ingredient_name)
                ingredient = ingredients[ingredient_name]
                amount = row["recipe_amount"]
                dish_description.add_ingredient_dependency(ingredient, amount)
            self.dishes.add(dish_description)
