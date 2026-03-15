from read import read_products
from write import invoice, restock, write_products
from operation import (
    calculate_selling_price, apply_offer, display_products,
    find_product, process_sale, process_restock
)

def main():
    '''
    Description:It is the main entry point. It takes data from the text file and displays
    a menu that contains
    -view products
    -process sale
    -restock product
    -exit from the program
    The data is updated to the text file after the invoice is generated or the product is sold or restocked
    
    Arguments:None
    
    Returns: None
    '''
    products = read_products("products.txt")
    
    while True:
        print("\nWECARE BEAUTY STORE MANAGEMENT")
        print("1. View Products")
        print("2. Process Sale")
        print("3. Restock Products")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            display_products(products)
        elif choice == "2":
            customer, purchases = process_sale(products)
            if purchases:
                invoice(customer, purchases)
                write_products("products.txt", products)
        elif choice == "3":
            supplier, restock_items = process_restock(products)
            if restock_items:
                restock(supplier, restock_items)
                write_products("products.txt", products)
        elif choice == "4":
            print("Thank you for using WeCare!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
