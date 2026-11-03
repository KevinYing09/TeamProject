from datetime import date
from typing import List, Optional


class ExpenseSplit:
    """Tracks individual member contributions toward a specific expense."""
    
    def __init__(self, split_id: str, user_id: str, amount_owed: float, is_paid: bool = False):
        self.split_id = split_id
        self.user_id = user_id
        self.amount_owed = amount_owed
        self.is_paid = is_paid  # Defaults to False until marked paid

    def mark_as_paid(self) -> None:
        """Updates payment status to True when a member settles their portion."""
        self.is_paid = True


class Expense:
    """Represents a financial transaction incurred during a trip."""
    
    def __init__(
        self,
        expense_id: str,
        description: str,
        amount: float,
        paid_by_user_id: str,
        expense_date: date,
        category: str,
        splits: Optional[List[ExpenseSplit]] = None
    ):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount  # Total transaction amount
        self.paid_by_user_id = paid_by_user_id  # User ID of the person who paid upfront
        self.date = expense_date
        self.category = category
        self.splits = splits if splits is not None else []  # Stores individual split records

    def calculate_per_person(self) -> float:
        """Calculates equal share amount per participating member."""
        if not self.splits:
            return 0.0
        return self.amount / len(self.splits)

    def split_equally(self, user_ids: List[str]) -> None:
        """Divides total amount equally among all provided user IDs."""
        if not user_ids:
            return
            
        per_person = self.amount / len(user_ids)
        
        # Create a new ExpenseSplit record for each participating user
        self.splits = [
            ExpenseSplit(
                split_id=f"split_{self.expense_id}_{idx}",
                user_id=uid,
                amount_owed=per_person,
                # Automatically mark as paid if this user is the person who paid the initial bill
                is_paid=(uid == self.paid_by_user_id)
            )
            for idx, uid in enumerate(user_ids)
        ]


class Trip:
    """Main controller holding overall trip data, budget, and tracked expenses."""
    
    def __init__(self, trip_id: str, title: str, total_budget: float):
        self.trip_id = trip_id
        self.title = title
        self.total_budget = total_budget
        self.expenses: List[Expense] = []  # Collection of all expenses linked to this trip

    def add_expense(self, expense: Expense) -> None:
        """Appends a new expense object to the trip's expense log."""
        self.expenses.append(expense)

    def calculate_total_expenses(self) -> float:
        """Sums up the transaction amount across all expenses in the trip."""
        return sum(exp.amount for exp in self.expenses)
