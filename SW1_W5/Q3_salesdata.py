def format_data():
    try:
        with open('sales.csv') as f:
            csv = f.read().splitlines()
            data = []
            for entry in csv:
                entry = entry.split(';')
                mydict = {
                    'date': entry[0],
                    'total': int(entry[1]),
                    'price': float(entry[2])
                }
                data.append(mydict)
            return data
    except FileNotFoundError:
        print("File not found")
        return []

def calculate_total(data):
    total_amount = 0
    for element in data:
        amount = element['total'] * element['price']
        total_amount += amount
    print(f"The total amount to pay is {total_amount}")


if __name__ == '__main__':
    data = format_data()
    calculate_total(data)
