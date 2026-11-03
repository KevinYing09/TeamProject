class ExpenseSplit:
    # Tracks one user's share of an expense
    def __init__(self, user_id, amount_owed):
        self.user_id = user_id
        self.amount_owed = amount_owed
        self.is_paid = False  # Starts as unpaid by default


class Expense:
    # Represents a single cost (like dinner or gas)
    def __init__(self, description, amount, paid_by_user_id):
        self.description = description
        self.amount = amount
        self.paid_by_user_id = paid_by_user_id  # Who paid the upfront bill
        self.splits = []  # Holds ExpenseSplit objects for everyone sharing the cost

    # Divides the total cost equally among all users
    def split_equally(self, user_ids):
        per_person = self.amount / len(user_ids)
        for uid in user_ids:
            split = ExpenseSplit(uid, per_person)
            # Mark as paid automatically for the person who paid upfront
            if uid == self.paid_by_user_id:
                split.is_paid = True
            self.splits.append(split)


class Trip:
    # Holds all trip details and list of expenses
    def __init__(self, title, total_budget):
        self.title = title
        self.total_budget = total_budget
        self.expenses = []  # Holds Expense objects added to this trip

    # Adds up the total amount of all expenses on the trip
    def calculate_total_expenses(self):
        return sum(e.amount for e in self.expenses)
