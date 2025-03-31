from flask import Flask, render_template, request, redirect
import webbrowser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/payment', methods=['POST'])
def payment():
    name = request.form.get("name")
    age = request.form.get("age")
    height = request.form.get("height")
    weight = request.form.get("weight")
    package_choice = request.form.get("package")
    payment_method = request.form.get("payment_method")

    package_dict = {
        "1": "Regular",
        "2": "Premium",
        "3": "VIP",
        "4": "Super Rich",
        "5": "Mega Rich"
    }
    
    if package_choice not in package_dict:
        return "Invalid package choice", 400

    payment_links = {
        "1": "https://uday-tech-dev.github.io/Uday-upi/",
        "2": "https://uday-tech-dev.github.io/Uday-Bank/",
        "4": "https://uday-tech-dev.github.io/cheque/"
    }
    
    if payment_method in payment_links:
        return redirect(payment_links[payment_method])
    elif payment_method == "3":
        return "Please provide cash to the doctor. Thank you for choosing us!"
    else:
        return "Invalid payment method", 400

if __name__ == "__main__":
    app.run(debug=True)

