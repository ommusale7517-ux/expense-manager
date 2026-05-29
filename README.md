# Expense Manager

A simple command-line application for tracking and visualizing personal expenses.

## Features

- ✅ **Add Expense** - Record new expenses with description, amount, and category
- ✅ **View Expenses** - Display all recorded expenses in a formatted list
- ✅ **Calculate Total** - Get the sum of all expenses
- ✅ **Visualize Data** - Generate bar charts showing expenses by category

## Requirements

- Python 3.x
- matplotlib (for graph visualization)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ommusale7517-ux/expense-manager.git
cd expense-manager
```

2. Install dependencies:
```bash
pip install matplotlib
```

## Usage

Run the application:
```bash
python expense_manager.py
```

### Menu Options

1. **Add Expense** - Enter expense details (description, amount, category)
2. **View Expenses** - List all recorded expenses
3. **Total Expense** - Calculate total expenses
4. **Show Graph** - Display expense breakdown by category as a bar chart
5. **Exit** - Close the application

### Example Workflow

```
1. Select "Add Expense"
2. Enter description: "Groceries"
3. Enter amount: 500
4. Enter category: "Food"
5. Select "View Expenses" to see all transactions
6. Select "Show Graph" to visualize spending by category
```

## Categories

The application supports the following expense categories:
- **Food** - Groceries, restaurants, dining
- **Travel** - Transportation, fuel, commute
- **Utilities** - Bills, subscriptions, services

## Notes

- All expenses are stored in memory during the session
- Data is not persisted between sessions (future enhancement)
- Enter valid numerical amounts when prompted
- The rupee symbol (₹) is used as the currency

## Future Enhancements

- [ ] Persist expenses to a database
- [ ] Export expenses to CSV
- [ ] Add date/time tracking
- [ ] Set budget limits
- [ ] More category options
- [ ] Search/filter functionality

## License

MIT License

## Author

Created with ❤️ for expense tracking