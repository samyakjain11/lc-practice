import spreadsheet_utils

PARTICIPANTS_SPREADSHEET_ID = '1ruZNZID80X0TY0Bj17_Bcd2axxyM1kHs8UmKR1R8l4M'

def addExpense(expenseName, expenseAmount, expenseCategory, num_entries:int) -> bool:
    values = [[expenseName, expenseAmount, expenseCategory]]
    spreadsheet_utils.insert_row(spreadsheet_id=PARTICIPANTS_SPREADSHEET_ID, num_rows=num_entries, values=values, num_fields=3)
    # send this via email with gmail API
    # free upto 1 billion requests / day