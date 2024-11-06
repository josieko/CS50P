from project import BudgetTracker


def test_add_spending():
    tracker = BudgetTracker()

    transaction = tracker.add_spending(100.50, "food", "Groceries")
    assert transaction["amount"] == 100.50
    assert transaction["category"] == "food"
    assert transaction["description"] == "Groceries"
    assert "date" in transaction


def test_get_spendings():
    tracker = BudgetTracker()

    tracker.add_spending(100, "food", "Groceries")
    tracker.add_spending(50, "transport", "Gas")

    transactions = tracker.get_spendings()
    assert len(transactions) == 2
    assert transactions[0]["amount"] == 100
    assert transactions[1]["amount"] == 50


def test_get_summary():
    tracker = BudgetTracker()

    tracker.add_spending(100, "food", "Groceries")
    tracker.add_spending(50, "food", "Restaurant")
    tracker.add_spending(30, "transport", "Gas")

    summary = tracker.get_summary()
    assert summary["food"] == 150
    assert summary["transport"] == 30
