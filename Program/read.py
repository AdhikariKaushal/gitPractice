def read_products(filename="products.txt"):
    '''
    Description:
        to read the text from the text file and keep in the list of dictionaries
        Each line in the file should contain the details of product such as name, brand, stock, CP and origin
    Args:
        filename(str):The name of the file from where we read
    Returns:
        list:A list of dictonaries each representing product with their keys
            'name' (str),"brand"(Str),"stock"(Str),"CP"(float) and "origin"(Str)
    '''
    products = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) == 5:
                product = {
                    'name': parts[0],
                    'brand': parts[1],
                    'stock': int(parts[2]),
                    'cost_price': float(parts[3]),
                    'origin': parts[4]
                }
                products.append(product)
    return products


