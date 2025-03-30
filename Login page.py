import tkinter as tk
from tkinter import messagebox
import webbrowser

# User credentials
users = {
    "Uday": "Intelligent",
    "Amma": "Intelligent",
    "Aachi": "Intelligent",
    "Baba": "Intelligent",
    "Mithun": "Idiot"
}


# Function to check login
def check_login():
    username = username_entry.get()
    password = password_entry.get()

    if users.get(username) == password:
        messagebox.showinfo("Login Successful", "Redirecting to website...")
        webbrowser.open("https://uday-tech-dev.github.io/Uday-food-company/")
    else:
        messagebox.showerror("Login Failed", "Invalid credentials. Try again.")


# Create Tkinter window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

# Labels
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")  # Hide password input
password_entry.pack()

# Login Button
login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack(pady=10)

# Run the GUI
root.mainloop()


