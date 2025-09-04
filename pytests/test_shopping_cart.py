from shopping_cart import ShoppingCart
import pytest
from pytest import fixture
from item_database import ItemDatabase
from unittest.mock import Mock

#fixture helps to create a reliable basline for tests
@fixture
def cart():
    return ShoppingCart(5)

def test_can_add_item(cart):
    cart.add("apple")
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()
    
def test_when_add_more_than_max(cart):
    with pytest.raises(OverflowError):
        for _ in range(6):
            cart.add("blue")
        
def test_can_get_total_price(cart):
    cart.add("apple")
    cart.add("orange")
    item_database = ItemDatabase()
    
    def mock_get_item(item:str):
        if item == "apple":
            return 1.0
        elif item == "orange":
            return 2.0
    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == 3.0