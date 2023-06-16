from src.models.ingredient import (Ingredient, Restriction,)  # noqa: F401, E261, E501


def test_ingredient():
    bacon = Ingredient("bacon")
    assert bacon.name == "bacon"
    assert bacon.restrictions == {Restriction.ANIMAL_MEAT}
    assert repr(bacon) == "Ingredient('bacon')"

    test_bacon = Ingredient("bacon")
    assert bacon.__hash__() == test_bacon.__hash__()
    assert bacon == bacon

    test_farinha = Ingredient("farinha")
    assert bacon.__hash__() == test_farinha.__hash__()
    assert bacon != test_farinha