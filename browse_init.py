from products import dao


class Product:
    def _init_(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data):
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    # Fetch all products in one go and load them using a list comprehension
    products = dao.list_products()
    return [Product.load(product) for product in products]


def get_product(product_id: int) -> Product:
    # Fetch the product and directly load it
    product_data = dao.get_product(product_id)
    if not product_data:
        raise ValueError(f"Product with id {product_id} not found")
    return Product.load(product_data)


def add_product(product: dict):
    # Perform lightweight validation here if needed
    if 'id' not in product or 'name' not in product:
        raise ValueError("Product must contain at least 'id' and 'name'")
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError("Quantity cannot be negative")
    # Directly update the quantity in the database
    dao.update_qty(product_id, qty)
