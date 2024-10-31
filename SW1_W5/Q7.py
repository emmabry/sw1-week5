import csv
import os


def write_headers():
    file_exists = os.path.isfile('pet_data.csv')
    with open('pet_data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        if not file_exists:
            writer.writerow(["Chip number", "Name", "Breed", "Gender"])


def add_pet():
    fields = []
    headers = ['Chip number', 'Name', 'Breed', 'Gender']
    chip_number = input("Enter your pets microchip number: ")
    fields.append(chip_number)
    pet_name = input("Enter your pet name: ")
    fields.append(pet_name)
    pet_breed = input("Enter your pet breed: ")
    fields.append(pet_breed)
    pet_gender = input("Enter your pet gender: ")
    fields.append(pet_gender)

    with open('pet_data.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(fields)
    print("Your pet data has been added.\n")


def search_pet():
    method = ""
    while method not in {"chip", "name"}:
        method = input("Do you want to find the pet by 'chip' or 'name'? ").strip().lower()
        if method not in {"chip", "name"}:
            print("Invalid input. Please enter 'chip' or 'name'.")
    search_value = input("Enter your pet's chip number: ").strip() if method == "chip" else input(
        "Enter your pet's name: ").strip().lower()

    with open('pet_data.csv', 'r') as f:
        mydict = csv.DictReader(f, delimiter=';')
        found = False
        for row in mydict:
            if search_value == row.get('Name').lower() or search_value == row.get('Chip number'):
                found = True
                print(row)
        if not found:
            print("Your pet data has not been found.")


def print_summary():
    rows = []
    with open('pet_data.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            rows.append(row)

    print("PET REPORT")
    print("==========")
    for row in rows:
        print(
            f"Pet chip number: {row['Chip number']}, Pet name: {row['Name']}, pet breed: {row['Breed']}, pet gender: {row['Gender']} \n")


def main():
    write_headers()
    while True:
        print("Welcome to Find My Pet")
        print("Please select one of the options:")
        print("1. Add a pet")
        print("2. Search a pet's details")
        print("3. Print a summary of all pets")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    add_pet()
                case 2:
                    search_pet()
                case 3:
                    print_summary()
                case 4:
                    break
        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
