from flask import Blueprint, request

# Create Blueprint
api = Blueprint("api", __name__)

# Add Bill
@api.route("/add_bill", methods=["GET", "POST"])
def add_bill():
    if request.method != "POST":
        return "Whoops, this page only takes POST requests."

# Add Spend
@api.route("/add_spend", methods=["GET", "POST"])
def add_spend():
    if request.method != "POST":
        return "Whoops, this page only takes POST requests."

# Add Account
@api.route("/add_account", methods=["GET", "POST"])
def add_account():
    if request.method != "POST":
        return "Whoops, this page only takes POST requests."

# Edit Account
@api.route("/edit_account", methods=["GET", "POST"])
def edit_account():
    if request.method != "POST":
        return "Whoops, this page only takes POST requests."

# Edit Bill
@api.route("/edit_bill", methods=["GET", "POST"])
def edit_bill():
    if request.method != "POST":
        return "Whoops, this page only takes POST requests."

# Edit Spend
@api.route("/edit_spend", methods=["GET", "POST"])
def edit_spend():
    if request.method != "POST":
        return "Whoops, this page only takes POST requests."
