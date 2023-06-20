import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    
    tomate = Ingredient("tomate")
    lasanha = "lasanha presunto"
    price = 25.90
    dish = Dish("lasanha presunto", 25.90)
    
    assert dish.name == "lasanha presunto"
    assert dish.price == 25.90
    
    dish.add_ingredient_dependency(tomate, 10)
    assert dish.recipe.get(tomate) == 10
    assert dish.get_ingredients() == {tomate}
    
    with pytest.raises(TypeError):
        assert Dish("lasanha presunto", "22.90")
    
    with pytest.raises(ValueError):
        assert Dish("lasanha presunto", -22.90)
        
    assert dish.get_restrictions() == set()
    
    test_lasanha = Dish("lasanha presunto", 25.90)
    assert dish.__hash__() == test_lasanha.__hash__()
    assert dish == test_lasanha
    
    test_cheep_lasanha = Dish("lasanha apresuntado", 20.90)
    assert dish.__hash__() != test_cheep_lasanha.__hash__()
    assert dish != test_cheep_lasanha

    dish_test = Dish(lasanha, price)
    assert dish_test.name == lasanha
    assert repr(dish_test) == f"Dish('{lasanha}', R${price:.2f})"
