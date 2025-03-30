import webbrowser
import sys

def redirect_to_upi():
    url = "https://uday-tech-dev.github.io/Uday-upi/"
    webbrowser.open(url)

def redirect_to_uday_bank():
    url = "https://uday-tech-dev.github.io/Uday-Bank/"
    try:
        webbrowser.open(url, new=2)  # Opens in a new tab if possible
        print("Redirecting to Uday Bank...")
    except Exception as e:
        print("Error opening the browser:", e)

print("Welcome to Uday hospitals")
Name = input("Name:")
Age = int(input("Age:"))
if Age < 18:
    print("You must be 18+ to proceed")
    sys.exit()
if Age > 100:
    print("Please enter a valid age")
    sys.exit()
Height = int(input("Height(in cm):"))
if Height < 175:
    print("Please enter a valid height")
    sys.exit()
Weight = int(input("Weight(in kg):"))
if Weight < 65:
    print("Please enter a valid Weight")
    sys.exit()

while True:
    print("Please choose a package:")
    print("1. Regular(200 rs)")
    print("2. Premium(1000 rs)")
    print("3. VIP(5000 rs)")
    choice = input("Enter your choice (1/2/3): ")
    if choice in ["1", "2", "3"]:
        print(f"You selected {'Regular' if choice == '1' else 'Premium' if choice == '2' else 'VIP'} package.")
        break
    else:
        print("Invalid choice, please enter 1, 2, or 3.\n")

print("Please choose payment method")
print("1. UPI (You will be redirected to Uday UPI)")
print("2. Credit card (You will be redirected to Uday Bank)")
print("3. Cash (You will provide the money to the doctor)")
Choice = input("Enter your choice (1/2/3): ")

if Choice == "1":
    redirect_to_upi()
elif Choice == "2":
    redirect_to_uday_bank()
elif Choice == "3":
    print("Doctor will be with you shortly. You can pay him directly.")
else:
    print("Invalid payment choice.")

print("Thank you for booking an appointment!")
