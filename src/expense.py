from datetime import date
from typing import List, Optional


class ExpenseSplit:
    def __init__(self, split_id: str, user_id: str, amount_owed: float, is_paid: bool = False):
        self.split_id = split_id
        self.user_id = user_id
        self.amount_owed = amount_owed
        self.is_paid = is_paid

    def mark_as_paid(self) -> None:
        self.is_paid = True


class Expense:
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
        self.amount = amount
        self.paid_by_user_id = paid_by_user_id
        self.date = expense_date
        self.category = category
        self.splits = splits if splits is not None else []

    def calculate_per_person(self) -> float:
        if not self.splits:
            return 0.0
        return self.amount / len(self.splits)

    def split_equally(self, user_ids: List[str]) -> None:
        if not user_ids:
            return
        per_person = self.amount / len(user_ids)
        self.splits = [
            ExpenseSplit(
                split_id=f"split_{self.expense_id}_{idx}",
                user_id=uid,
                amount_owed=per_person,
                is_paid=(uid == self.paid_by_user_id)
            )
            for idx, uid in enumerate(user_ids)
        ]


class Trip:
    def __init__(self, trip_id: str, title: str, total_budget: float):
        self.trip_id = trip_id
        self.title = title
        self.total_budget = total_budget
        self.expenses: List[Expense] = []

    def add_expense(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def calculate_total_expenses(self) -> float:
        return sum(exp.amount for exp in self.expenses)
