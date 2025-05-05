from unittest.mock import Mock
from shopping_cart import ShoppingCart
import pytest

from item_database import ItemDb


# pytest fixture: it reduces the repetitive code, i have cart in all function let's handle with it using fixtures

@pytest.fixture
def cart():
    return ShoppingCart(5)


def test_can_add_item_to_cart(cart):
    # cart = ShoppingCart(5) # now i don't this because i have initalized pytest fixtures for cart,
    #  i just have to pass cart as an argument

    cart.add('apple')

    cart.add('banaba')

    assert cart.size() ==2


def test_item_added_in_cart_or_not(cart):

    # cart = ShoppingCart(5)

    cart.add('apple')

    assert "apple" in cart.get_item()


def test_for_more_items(cart):

    # cart = ShoppingCart(5)

    with pytest.raises(OverflowError):
        for _ in range(6):
            cart.add('mangos')


def test_get_total_pricee(cart):
    # cart = ShoppingCart(5)
    cart.add('appel')
    cart.add('apple')



    # mapp = {
    #     "appel": 11,
    #     "apple": 12
    # }

    itemdb = ItemDb()

    def get_mock_item(item: str):
        if item == "appel":
            return 11
        if item == 'apple':
            return 12
    itemdb.get = Mock(side_effect=get_mock_item)

    assert cart.get_total_price(itemdb) == 23

    print('Testing')



# Testing specific function pytest filename::function_name



