#!/usr/bin/env python


from flask import Flask, render_template, request
from database import Database

# Create flask object
app = Flask(__name__)

path = "data/db.xml"
db = Database(path)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        acct_id = request.form["acctid"]
        acct_balance = db.balance(acct_id.upper())
        app.logger.debug(f"Balance for {acct_id}: {acct_balance}")

    else:
        acct_balance = "N/A"

    return render_template("./index.html", acct_balance=acct_balance)

if __name__ == '__main__':
    app.run(host='localhost',port=8080, debug =True)


#if __name__ == "__main__":
 #   print(f"Beginning START.PY; {__name__}")
  #  app.run(host="0.0.0.0", debug=True)
