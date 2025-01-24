import json
from typing import List, Optional
from cart import dao
from products import Product, get_product


class Cart:
    def _init_(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> 'Cart':
        contents = [get_product(product_id) for product_id in data['contents']]
        return Cart(data['id'], data['username'], contents, data['cost'])


def get_cart(username: str) -> List[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    products_in_cart = []
    for cart_detail in cart_details:
        try:
            contents = json.loads(cart_detail['contents'])
            products_in_cart.extend(contents)
        except (json.JSONDecodeError, TypeError):
            continue

    return [get_product(product_id) for product_id in products_in_cart]


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)
