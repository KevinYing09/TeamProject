#Tristan Medford
class ExpenseSplit:
    # Tracks how much one person owes
    def __init__(self, user_id, amount_owed):
        self.user_id = user_id
        self.amount_owed = amount_owed
        self.is_paid = False


class Expense:
    # Represents a single item bought
    def __init__(self, amount, paid_by_user_id):
        self.amount = amount
        self.paid_by_user_id = paid_by_user_id
        self.splits = []

    # Splits the total cost equally among everyone
    def split_equally(self, user_ids):
        cost_per_person = self.amount / len(user_ids)
        for uid in user_ids:
            split = ExpenseSplit(uid, cost_per_person)
            split.is_paid = (uid == self.paid_by_user_id) 
            self.splits.append(split)
