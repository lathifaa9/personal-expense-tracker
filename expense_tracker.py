from decimal import Decimal, InvalidOperation

def get_positive_amount():
  """ Ask for an expense amount until the user enters a valid positive number."""
  while True:
    amount_text = input("amount : $").strip()

    try:
      amount = Decimal(amount_text)
    except InvalidOperation:
      print("Please enter a valid number, for example: 250.50")
      continue

    if amount <= 0:
      print("Sorry the amount should be greater than zero")
      continue

    return amount

def add_expense(expenses):
  """collect one expense from the user and store it in the list."""
  category = input("category: ").strip()
  description = input("Description : ").strip()
  amount = get_positive_amount()

  expense = {
    "category" : category,
    "description": description,
    "amount" : amount,
  }

  expenses.append(expense)
  print("Expense added successfully.")

def show_expenses(expenses):
  """display every expense currently stored in memory"""
  if not expenses:
    print("No expenses have been added yet.")
    return

  print("\n--- Your Expenses ---")
  total = Decimal ("0")

  for number, expense in enumerate(expenses, start=1):
    print(
      f"{number}. {expense['category']} |"
      f"{expense['description']} | ${expense['amount']}"
    )

    total += expense["amount"]

  print(f"Total spent: ${total}")

def main():
  expenses = []
  print("welcome to the personal expense tracker !")

  while True:
      print("\n1. Add expense")
      print("2. View expenses")
      print("3. Exit")

      choice = input("Choose an option (1-3): ").strip()

      if choice == "1":
        add_expense(expenses)
      elif choice == "2":
        show_expenses(expenses)
      elif choice == "3":
        print("Goodbye , have a nice day")
        break
      else:
        print("Invalid choice. please enter 1, 2 or 3")

if __name__ == "__main__":
    main()        