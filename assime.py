# COMMUNITY DATA PROCESSING SYSTEM

record = []

#AGE GROUP

def get_age_group(age):

    if age <= 5:

        return "Infant"

    elif age <= 17:

        return "Teenager"

    elif age <= 59:

        return "Adult"

    else:

        return "Aged"

#TO ADD RECORD

def add_record():

    while True:

        name = input("Enter Full Name: ")

        if name.replace(" ", "").isalpha():

            break

        else:

            print("Wrong entry. Name should contain only letters.")

    while True:

        age = input("Enter Age: ")

        if age.isdigit():

            age = int(age)

            break

        else:

            print("Wrong entry. Age should contain only digits.")

    address = input("Enter Your Address: ")

    email = input("Enter Your Email (optional): ")

    gender = input("Enter Your Gender: ")

    phone = input("Enter Your Phone: ")

    employment = input("Enter Your Employment Status (Employed/Unemployed): ")

    category = get_age_group(age)

    person = {

        "name": name,

        "age": age,

        "category": category,

        "gender": gender,

        "phone": phone,

        "address": address,

        "email": email,

        "employment": employment,

    }

    record.append(person)

    print("Record added successfully!")

#TO VIEW RECORDS

def view_record():

    if len(record) == 0:

        print("No record available.")

    else:

        print("\n===== All Records =====")

        for i, person in enumerate(record, start=1):

            print(f"\nRecord {i}")

            print("Name:", person["name"])

            print("Age:", person["age"])

            print("Category:", person["category"])

            print("Gender:", person["gender"])

            print("Phone:", person["phone"])

            print("Address:", person["address"])

            print("Email:", person["email"])

            print("Employment:", person["employment"])

#TO SEARCH RECORD

def search_record():

    if len(record) == 0:

        print("No record available.")

        return

    search_name = input("Enter Name to search: ").lower()

    found = False

    for person in record:

        if search_name in person["name"].lower():

            print("\nRecord Found")

            print("Name:", person["name"])

            print("Age:", person["age"])

            print("Category:", person["category"])

            print("Gender:", person["gender"])

            print("Phone:", person["phone"])

            print("Address:", person["address"])

            print("Email:", person["email"])

            print("Employment:", person["employment"])

            found = True

    if not found:

        print("Person not found.")

#TO SHOW STATISTICS

def show_statistics():

    if len(record) == 0:

        print("No record available.")

        return

    total = len(record)

    total_age = 0

    infant = teenager = adult = aged = 0

    employed = unemployed = 0

    for person in record:

        total_age += person["age"]

        if person["category"] == "Infant":

            infant += 1

        elif person["category"] == "Teenager":

            teenager += 1

        elif person["category"] == "Adult":

            adult += 1

        else:

            aged += 1

        if person["employment"].lower() == "employed":

            employed += 1

        elif person["employment"].lower() == "unemployed":

            unemployed += 1

    average_age = total_age / total

    print("\n===== COMMUNITY STATISTICS =====")

    print("Total Population:", total)

    print("Infants:", infant)

    print("Teenagers:", teenager)

    print("Adults:", adult)

    print("Aged:", aged)

    print("Employed:", employed)

    print("Unemployed:", unemployed)

    print("Average age:", round(average_age, 2))

#MENU LOOP

while True:

    print("\n==========================")

    print(" COMMUNITY DATA PROCESSING SYSTEM ")

    print("==========================")

    print("1. Add Record")

    print("2. View Record")

    print("3. Search Person")

    print("4. Show Statistics")

    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_record()

    elif choice == "2":

        view_record()

    elif choice == "3":

        search_record()

    elif choice == "4":

        show_statistics()

    elif choice == "5":

        print("Thank you for using the program!")

        break

    else:

        print("Wrong entry. Please choose 1 to 5.")