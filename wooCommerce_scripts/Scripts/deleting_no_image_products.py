
from WooCommerceUtility import WooCommerceUtility


def v1_deleting_products_without_images():
    # Set the desired number of products per page
    woo_helper = WooCommerceUtility()
    per_page = 100
    page = 1
    while True:
     # Retrieve products from current page

        products = woo_helper.get("products", params={'per_page': per_page, 'page': page})



        # Check if there are more products or if the response is empty
        if not products:
            print("No more products found.")
            break

        # Process the products as needed
        for product in products:
            images = product.get('images', [])
            if not images:
                product_id = product['id']
                product_name = product['name']
                deleted_item = woo_helper.delete(f"products/{product_id}", params={'force': True})
                print(f"Deleted product with ID: {product_id} and deleted product name: {product_name}")

        page += 1


if __name__ == "__main__":
    woo_helper = WooCommerceUtility()
    v1_deleting_products_without_images()

def v2_deleting_products_without_images():
    # Set products per page
    per_page = 100

    # Initialize the WooCommerceUtility
    woo_helper = WooCommerceUtility()

    response_headers = woo_helper.get("products", params={'per_page': 1}, return_headers=True)
    total_products = int(response_headers['headers']['X-WP-Totalpages'])

    total_pages = (total_products // per_page) + 1
    for page in range(1, total_pages+1):
        products = woo_helper.get("products", params={'per_page': per_page, 'page': page})

        for product in products:
            images = product.get('images', [])
            if not images:
                product_id = product['id']
                product_name = product['name']
                deleted_item = woo_helper.delete(f"products/{product_id}", params={'force': True})
                print(f"Deleted product with ID: {product_id} and deleted product name: {product_name}")
                print(deleted_item)
        else:
            print("No more products found.")


if __name__ == "__main__":
    v2_deleting_products_without_images()

