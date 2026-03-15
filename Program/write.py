from operation import custom_sum, calculate_vat
import datetime

def invoice(customer, purchases):
    '''
    Description:
        To generate  and save a sales invoice in the name of the customer with the name and print to the terminal
    Args:
        customername(string),
        purchases(list): A list of dictionaries, each representing the purchased item.
    Returns:none
    '''
    now = datetime.datetime.now()
    unique_value = str(now.minute) + str(now.second) + str(now.microsecond)
    filename = "sales_" + customer + "_" + unique_value + ".txt"

    total_amount = custom_sum(purchases)
    vat_rate = 13
    vat_amount, total_with_vat = calculate_vat(total_amount, vat_rate)

    lines = []
    lines.append(f"Customer: {customer}")
    lines.append("Date: " + now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    lines.append("Invoice Details")
    lines.append("-" * 80)
    lines.append(f"{'Product':<20} {'Qty':<8} {'Free Qty':<10} {'Unit Price':<15} {'Amount':<10}")
    lines.append("-" * 80)

    for item in purchases:
        name = item['product']['name']
        qty = item['quantity']
        free_qty = item['free_quantity']
        unit_price = item['product']['cost_price'] * 2
        amount = item['total_price']
        lines.append(f"{name:<20} {qty:<8} {free_qty:<10} {unit_price:<15.2f} {amount:<10.2f}")

    lines.append("-" * 80)
    lines.append(f"{'Total without VAT:':>65} {total_amount:.2f}")
    lines.append(f"{'VAT (' + str(vat_rate) + '%):':>65} {vat_amount:.2f}")
    lines.append(f"{'Total with VAT:':>65} {total_with_vat:.2f}")
    lines.append("-" * 80)

    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

    # Print to terminal
    print("\n".join(lines))
    print("Final invoice saved to", filename)


def restock(supplier, restock_items):
    '''
    Desription:
        To create and save the restock invoice in the name of supplier along with the time
    Args:
        supplier(Str):name of supplier of the product
        restock_item(list):
    Returns:
        none
    '''
    now = datetime.datetime.now()
    unique_value = str(now.minute) + str(now.second) + str(now.microsecond)
    filename = f"restock_{supplier}_{unique_value}.txt"
    total_amount = sum(item['cost_price'] * item['quantity'] for item in restock_items)
    vat_rate = 13
    vat_amount, total_with_vat = calculate_vat(total_amount, vat_rate)

    lines = []
    lines.append("=" * 70)
    lines.append("WECARE BEAUTY STORE - RESTOCK INVOICE")
    lines.append("=" * 70 + "\n")
    lines.append(f"Supplier: {supplier}")
    lines.append(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("-" * 70)
    lines.append(f"{'Product':<20} {'Brand':<15} {'Qty':<8} {'Unit Cost':<12} {'Amount':<10}")
    lines.append("-" * 70)

    for item in restock_items:
        amount = item['cost_price'] * item['quantity']
        lines.append(f"{item['name']:<20} {item['brand']:<15} "
                     f"{item['quantity']:<8} {item['cost_price']:<12.2f} {amount:<10.2f}")

    lines.append("-" * 70)
    lines.append(f"{'TOTAL AMOUNT:':>55} {total_amount:.2f}")
    lines.append(f"{'VAT (' + str(vat_rate) + '%):':>55} {vat_amount:.2f}")
    lines.append(f"{'Total with VAT:':>55} {total_with_vat:.2f}")
    lines.append("=" * 70)

    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

    # Print to terminal
    print("\n".join(lines))
    print(f"Restock invoice saved to {filename}")
    return filename




def write_products(filename="products.txt", products=[]):
    '''
    Description:
        to write the updated product after it has been sold or restock to the text file
    Args:
        filename(Str),
        products(list):The list with dictionaries
                        'name','brand','stock','CP','origin' '''
    with open(filename, "w") as file:
        for product in products:
            line = f"{product['name']}, {product['brand']}, {product['stock']}, {product['cost_price']}, {product['origin']}\n"
            file.write(line)
