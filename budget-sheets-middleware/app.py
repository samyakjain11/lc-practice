import util
from flask import Flask, request
import qrcode


app = Flask(__name__)

num_expenses = 0

# to build frontend with scanning qr codes:
# https://minhazav.medium.com/qr-code-scanner-using-html-and-javascript-3895a0c110cd
# https://blog.minhazav.dev/research/html5-qrcode.html
# https://stackoverflow.com/questions/36975619/how-to-call-a-rest-web-service-api-from-javascript

@app.route('/add-expense', methods = ["POST"])
def POST_add_expense():
    global num_expenses
    expenseName = request.form['expenseName']
    expenseCategory = request.form['expenseCategory']
    expenseAmount = request.form['expenseAmount']
    print(dict(request.form))
    util.addExpense(expenseName, expenseAmount, expenseCategory, num_expenses)
    num_expenses += 1
    return "ok", 200

    



