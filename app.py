from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask on Render!"

if __name__ == '__main__':
    app.run()

import webbrowser


def redirect_to_upi():
    return redirect("https://uday-tech-dev.github.io/Uday-upi/")

def redirect_to_uday_bank():
    return redirect("https://uday-tech-dev.github.io/Uday-Bank/")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    name = request.form.get("name")
    age = int(request.form.get("age"))
    height = int(request.form.get("height"))
    weight = int(request.form.get("weight"))

    if age < 18:
        return "You must be 18+ to proceed."
    if age > 100:
        return "Please enter a valid age."
    if height < 175:
        return "Please enter a valid height."
    if weight < 65:
        return "Please enter a valid weight."

    package = request.form.get("package")
    payment = request.form.get("payment")

    if payment == "1":
        return redirect_to_upi()
    elif payment == "2":
        return redirect_to_uday_bank()
    elif payment == "3":
        return "Doctor will be with you shortly. You can pay him directly."

    return "Thank you for booking an appointment!"

if __name__ == '__main__':
    app.run(debug=True)
