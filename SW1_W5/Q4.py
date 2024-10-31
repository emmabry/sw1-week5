def process_data():
    with open('sales1.csv', 'r') as csvfile:
        sales_file = csvfile.read().splitlines()
        sales_data = []
        for row in sales_file:
            values = row.split(';')
            sales_dict = {
                'order_id': values[0],
                'product_id': values[1],
                'cust_id': values[2],
                'quantity': int(values[3]),
                'sale_date': values[4]
            }
            sales_data.append(sales_dict)

    with open('product.csv', 'r') as csvfile:
        product_file = csvfile.read().splitlines()
        product_data = []
        for row in product_file:
            values = row.split(';')
            product_dict = {
                'product_id': values[0],
                'product_name': values[1],
                'price': float(values[2])
            }
            product_data.append(product_dict)

    with open('customer.csv', 'r') as csvfile:
        customer_file = csvfile.read().splitlines()
        customer_data = []
        for row in customer_file:
            values = row.split(';')
            customer_dict = {
                'cust_id': values[0],
                'cust_name': values[1],
                'age': int(values[2]),
                'location': values[3]
            }
            customer_data.append(customer_dict)
    return sales_data, product_data, customer_data


def calc_total_sales(sales_data, product_data):
    total_sales = 0
    print("TOTAL SALES FOR EACH PRODUCT: ")
    for row in sales_data:
        amount_sold = row['quantity']
        for prod_row in product_data:
            if prod_row['product_id'] == row['product_id']:
                name = prod_row['product_name']
                print(f"{name} sold {amount_sold} units")
                print(f"Revenue for {name}: £{amount_sold * prod_row['price']}\n")


def show_demographics(customer_data, sales_data):
    print("CUSTOMER DEMOGRAPHICS")
    for cust in customer_data:
        print(f"Age: {cust['age']}, location: {cust['location']}")
        for sale in sales_data:
            if sale['cust_id'] == cust['cust_id']:
                print(f"This customer bought product {sale['product_id']} \n")



if __name__ == '__main__':
    sales_data, product_data, customer_data = process_data()
    calc_total_sales(sales_data, product_data)
    show_demographics(customer_data, sales_data)
