from datetime import datetime


class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_spending(self, amount, category, description):
        transaction = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%d/%m/%y"),
        }
        self.transactions.append(transaction)
        return transaction

    def get_spendings(self):
        return self.transactions

    def get_summary(self):
        summary = {}
        for transaction in self.transactions:
            category = transaction["category"]
            amount = transaction["amount"]
            summary[category] = summary.get(category, 0) + amount
        return summary

    def display_summary(self):
        summary = self.get_summary()
        print("\nExpense Summary:")
        print("-" * 30)
        total = 0
        for category, amount in summary.items():
            print(f"{category.capitalize()}: ${amount:.2f}")
            total += amount
        print("-" * 30)
        print(f"Total: ${total:.2f}")


def main():
    tracker = BudgetTracker()
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. View Transactions")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")
            tracker.add_spending(amount, category, description)
        elif choice == "2":
            tracker.display_summary()
        elif choice == "3":
            transactions = tracker.get_spendings()
            for t in transactions:
                print(
                    f"{t['date']} - {t['category']} - ${t['amount']:.2f} - {t['description']}"
                )
        elif choice == "4":
            break


if __name__ == "__main__":
    main()
