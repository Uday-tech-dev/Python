import os
import sqlite3
import webbrowser

# Show current working directory
print("Current working directory:", os.getcwd())

# Create a connection to the SQLite database
conn = sqlite3.connect('uday_hospitals.db')
cursor = conn.cursor()

# Create the transactions table (with height & weight added)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        height INTEGER,
        weight INTEGER,
        package TEXT,
        payment_method TEXT
    )
''')
conn.commit()

print("Database 'uday_hospitals.db' created successfully!")
print("Welcome to Uday Hospitals")

# Collect user details
name = input("Name: ")
age = input("Age: ")
height = input("Height (in cm): ")
weight = input("Weight (in kg): ")

# Package Selection
package_dict = {
    "1": ("Regular", 200),
    "2": ("Premium", 1000),
    "3": ("VIP", 5000),
    "4": ("Super rich", 50000),
    "5": ("Mega Rich", 100000)
}

print("\nPlease choose a package:")
for key, value in package_dict.items():
    print(f"{key}. {value[0]} ({value[1]} rs)")
package_choice = input("Enter your choice (1/2/3/4/5): ")

if package_choice not in package_dict:
    print("Invalid choice. Exiting...")
    exit()

selected_package, amount = package_dict[package_choice]
print(f"You selected {selected_package} package.")

# Payment Method Selection
payment_methods = {
    "1": "UPI",
    "2": "Credit Card",
    "3": "Cash",
    "4": "Digital Cheque"
}

print("\nPlease choose a payment method:")
for key, value in payment_methods.items():
    print(f"{key}. {value}")

choice = input("Enter your choice (1/2/3/4): ")

payment_links = {
    "1": "https://uday-tech-dev.github.io/Uday-upi/",
    "2": "https://uday-tech-dev.github.io/Uday-Bank/",
    "4": "https://uday-tech-dev.github.io/cheque/"
}

if choice in payment_methods:
    payment_method = payment_methods[choice]
    if choice in payment_links:
        webbrowser.open(payment_links[choice])
    elif choice == "3":
        print("Please provide the money to the doctor")
else:
    print("Invalid choice. Exiting...")
    exit()

# Store transaction in database (now after choosing payment)
cursor.execute('''
INSERT INTO transactions (name, age, height, weight, package, payment_method)
VALUES (?, ?, ?, ?, ?, ?)
''', (name, age, height, weight, selected_package, payment_method))
conn.commit()

# Receipt
receipt_links = {
    "1": "https://uday-tech-dev.github.io/Uday-Receipt-Regular/",
    "2": "https://uday-tech-dev.github.io/Uday-Receipt-Premium/",
    "3": "https://uday-tech-dev.github.io/Uday-Receipt-VIP/"
}

if package_choice in receipt_links:
    webbrowser.open(receipt_links[package_choice])

print("Thank you for choosing Uday Hospitals!")

# Close database connection
cursor.close()
conn.close()

# ======================= Rating System =======================
def display_ratings():
    """Function to display current ratings from 'ratings.txt'"""
    if os.path.exists("ratings.txt"):
        with open("ratings.txt", "r") as file:
            ratings = file.readlines()
            if ratings:
                print("\nCurrent Ratings:")
                for line in ratings:
                    print(line.strip())
            else:
                print("\nNo ratings yet.")
    else:
        print("\nNo ratings yet.")

def save_rating(rating, comment):
    """Function to save the new rating"""
    with open("ratings.txt", "a") as file:
        file.write(f"Rating: {rating}/5, Comment: {comment}\n")
    print("\nThank you for your rating!")

def main():
    """Main function for collecting user rating"""
    print("\nWelcome to the Rating Page!")
    display_ratings()

    # Collect


    
