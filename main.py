from flask import Flask, render_template, request, redirect
from sql import select

# Create Flask app
app = Flask(__name__)

# API Blueprint
from api import api
app.register_blueprint(api, url_prefix="/api")

# Load Index page
@app.route("/")
def index():
    return render_template("index.html")



# --------------- BILLS --------------- #

# Bills page
@app.route("/bills")
def bills():
    bills = select("bills")
    return render_template("bills.html", bills=bills)

# Add Bill page
@app.route("/bills/add")
def bills_add():
    return render_template("bills_add.html")

# Edit Bill page
@app.route("/bills/edit")
def bills_edit():
    return render_template("bills_edit.html")

# --------------- SPENDING --------------- #

# Spending page
@app.route("/spending")
def spending():
    spending = select("spending")
    return render_template("spending.html", spending=spending)

# Add Spending page
@app.route("/spending/add")
def spending_add():
    accounts = select("accounts")
    return render_template("spending_add.html", accounts=accounts)

# Edit Spending page
@app.route("/spending/edit")
def spending_edit():
    return render_template("spending_edit.html")

# --------------- ACCOUNTS --------------- #

# Accounts page
@app.route("/accounts")
def accounts():
    accounts = select("accounts")
    return render_template("accounts.html", accounts=accounts)

# Add Account page
@app.route("/accounts/add")
def accounts_add():
    return render_template("accounts_add.html")

# Edit Account page
@app.route("/accounts/edit")
def accounts_edit():
    return render_template("accounts_edit.html")



# Run Flask app on load
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
