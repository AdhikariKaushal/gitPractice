def calculate_selling_price(cost_price, markup=2.0):
    """
    Description:
        Calculates the Selling price of the product with 200% from the cost price
    
    Args:
        cost_proce(float): CP of the product
        markup(float)

    Returns:
        float: SP of the product
       """
    return cost_price * markup

def apply_offer(quantity, cost_price):
    '''
    Description:
        Applies the "Buy 3 get 1 policy" and calculates the total price
    Args:
        quantity(int): no of items
        costprice(float): cost of each item
    Returns:
        tuple: total quantity(int),
            total price(float),
            free items(int)
    '''
    free_items = quantity // 3
    total_quantity = quantity + free_items
    total_price = calculate_selling_price(cost_price) * quantity
    return total_quantity, total_price, free_items

def custom_sum(purchases):
    '''
    Description:
        to calculate the total price of the items that have been purchased
    Args:
        purchases(list): total price of each item
    Returns:
        float:total amount
    '''
    total = 0
    for item in purchases:
    
        total += item['total_price']
    return total

def display_products(products):
    '''
    Description:
        to display the available products
    Args:
        product(list): list of product dictionaries
    Returns:
        None
    '''
    print("\nProduct Information")
    print("-" * 80)
    print(f"{'Name':<20} {'Brand':<15} {'Stock':<10} {'Price':<15} {'Origin':<15}")
    print("-" * 80)
    for p in products:
        print(
            f"{p['name']:<20} {p['brand']:<15} "
            f"{p['stock']:<10} {calculate_selling_price(p['cost_price']):<14.2f} "
            f"{p['origin']:<15}"
        )
    print("-" * 80)

def find_product(products, name):
    '''
    Description: 
        to search the product from the list
    Args:
        product(list): list of product dictionaries
        name(str):name of the product
    Returns:
        dictionary if product is found otherwise none
    '''
    for p in products:
        if p['name'].lower() == name.lower():
            return p
    return None

def process_sale(products):
    '''
    Description:
        To sale product by asking customer name, product name, quantity and to apply offer
    Args:
        products(list): list of product dictionaries
    Returns:
        tuple:Customer name(Str),
            list of purchases(list of dictionaries)
    '''
    while True:
        customer = input("Enter customer name: ").strip()
        if customer.replace(" ", "").isalpha():
            break
        else:
            print("Please enter a valid name.")

    purchases = []
    while True:
        display_products(products)
        product_name = input("\nEnter product name: ").strip()
        product = find_product(products, product_name)
        if not product:
            print("Product not found!")
            continue

        while True:  # Loop for quantity input
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive!")
                    continue

                total_qty, total_price, free = apply_offer(quantity, product['cost_price'])

                if total_qty > product['stock']:
                    print(f"Insufficient stock! Available: {product['stock']}")
                    continue

                product['stock'] -= total_qty
                purchases.append({
                    'product': product,
                    'quantity': quantity,
                    'free_quantity': free,
                    'total_price': total_price
                })

                print(f"Added {quantity} of {product['name']} to invoice.")
                break  # Exit the quantity loop once the valid quantity is entered

            except ValueError:
                print("Invalid quantity entered! Please enter a valid number.")
                continue  # This will prompt the user to re-enter the quantity for the same product

        # YES/NO validation for adding more products to the invoice
        while True:
            again = input("Do you want to buy another product? (yes/no): ").strip().lower()
            if again in ["yes", "no"]:
                break
            print("Please enter 'yes' or 'no'.")

        if again == "no":
            break

    return customer, purchases


def process_restock(products):
    """
    Description:
        Handles restocking of products by prompting the supplier for product details,
        validates input, updates existing product stock or adds new products, and
        returns the restocked items and supplier name.

    Args:
        products (list): A list of dictionaries, each representing a product.

    Returns:
        tuple: Supplier name (str) and a list of restocked items (list of dicts).
    """
    while True:
        supplier = input("Enter supplier name: ").strip()
        if supplier.replace(" ", "").isalpha():
            break
        else:
            print("Please enter a valid name.")

    restock_items = []

    while True:
        product_name = input("\nEnter product name to restock: ").strip()
        product = find_product(products, product_name)

        # Get valid quantity
        while True:
            try:
                quantity = int(input("Enter restock quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive!")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a number for quantity.")

        # Get valid cost price
        while True:
            try:
                unit_cost = float(input(f"Enter cost price for {product_name}: "))
                if unit_cost <= 0:
                    print("Cost price must be positive!")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a number for cost price.")

        # Update or add product
        if product:
            product['stock'] += quantity
            product['cost_price'] = unit_cost
            brand = product['brand']
            origin = product['origin']
        else:
            brand = input("Enter brand: ").strip()
                
            # Validate origin
            while True:
                origin = input("Enter origin: ").strip()
                if origin.replace(" ", "").isalpha():
                    break
                else:
                    print("Please enter a valid origin.")

            product = {
                'name': product_name,
                'brand': brand,
                'stock': quantity,
                'cost_price': unit_cost,
                'origin': origin
            }
            products.append(product)

        restock_items.append({
            'name': product_name,
            'brand': brand,
            'quantity': quantity,
            'cost_price': unit_cost
        })

        # YES/NO validation
        while True:
            again = input("Do you want to restock another product? (yes/no): ").strip().lower()
            if again in ["yes", "no"]:
                break
            print("Please enter 'yes' or 'no'.")

        if again == "no":
            break

    return supplier, restock_items


def calculate_vat(amount, rate=13):
    '''
    Description:
        To calculate VAT and total amount with VAT
    Args:
        amount(float):Total amount after VAT
        Rate(float):Rate of VAT
    Returns:
        tuple:VAT amount(float),
        Total amount with VAT(Float)
    '''
    vat_amount = (amount * rate) / 100
    total_with_vat = amount + vat_amount
    return vat_amount, total_with_vat
