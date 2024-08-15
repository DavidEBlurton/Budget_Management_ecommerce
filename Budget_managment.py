class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name  # Private attribute for category name
        self.__budget = budget  # Private attribute for allocated budget
        self.__remaining_budget = budget  # Initialize remaining budget

    # Getter for category name
    def get_name(self):
        return self.__name
    # Setter for category name
    def set_name(self, name):
        self.__name = name

    # Getter for allocated budget
    def get_budget(self):
        return self.__budget

    # Setter for allocated budget with validation
    def set_budget(self, budget):
        if budget > 0:
            self.__budget = budget
            self.__remaining_budget = budget
        else:
            print("Budget must be a positive number.")

    # Method to add an expense
    def add_expense(self, amount):
        if amount > 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
            else:
                print("Expense exceeds remaining budget.")
        else:
            print("Expense must be a positive number.")

    # Method to display category details
    def display_category_summary(self):
        print(f"Category: {self.__name}")
        print(f"Allocated Budget: ${self.__budget:.2f}")
        print(f"Remaining Budget: ${self.__remaining_budget:.2f}")


def main():
    categories = {}
    
    while True:
        print('''\nPersonal Budget Management System
        1. Add New Category
        2. Add Expense
        3. Display Category Summary
        4. Exit''')

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter category name: ").lower
            budget = float(input("Enter allocated budget: "))
            if budget > 0:
                categories[name] = BudgetCategory(name, budget)
                print(f"Category '{name}' added with a budget of ${budget:.2f}.")
            else:
                print("Budget must be a positive number.")

        elif choice == '2':
            name = input("Enter category name to add expense to: ")
            if name in categories:
                amount = float(input("Enter expense amount: "))
                categories[name].add_expense(amount)
            else:
                print("Category not found.")

        elif choice == '3':
            name = input("Enter category name to display summary: ").lower
            if name in categories:
                categories[name].display_category_summary()
            else:
                print("Category not found.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
