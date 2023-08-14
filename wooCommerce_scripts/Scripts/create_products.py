import random
import string
from WooCommerceUtility import WooCommerceUtility


def generate_random_string(length=10, prefix=None, suffix=None):
    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))
    if prefix:
        random_string = prefix + random_string
    if suffix:
        random_string = random_string + suffix
    return random_string


def create_100_simple_products():
    # Set up WooCommerce API client
    woo_helper = WooCommerceUtility()

    for i in range(1, 101):
        # Generate data for each product
        payload = {
            "name": generate_random_string(),
            "type": "simple",
            "regular_price": "10.99"
        }

        # Make API call to create product
        products_rs = woo_helper.wcapi.post("products", payload)

        if products_rs.status_code == 201:
            print(f"Product {i} created successfully")
        else:
            print(f"Error creating product {i}: {products_rs.status_code}")


# Call the function to create products
create_100_simple_products()


