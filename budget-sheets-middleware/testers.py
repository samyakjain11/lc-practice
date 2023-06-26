import requests

data = {"expenseName": "coffee", "expenseAmount": "100", "expenseCategory": "food_test"}

requests.post("http://127.0.0.1:5000/add-expense", data=data)
