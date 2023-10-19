# About MyDollarBot's /expense Feature
This feature enables the user to add/update/delete their expense in a pre-existing category.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/ebanigogia/dollar_bot/blob/main/code/expense.py)

# Code Description
## Functions

1. process_expense_command Function:
This function handles the initial expense-related command from a user.
It sends a message to the user with a keyboard markup that allows them to choose from options: "Add," "Delete," or "Update."
It registers a callback function (expense_option_selection) to handle the user's choice.

2. expense_option_selection Function:
This function is called when the user selects an option from the keyboard markup.
Depending on the selected option ("Add," "Delete," or "Update"), it directs the user to the respective function to perform that action.

3. select_expense_category Function:
This function is used to select the category for an expense.
It sends a message with a keyboard markup containing expense categories.
It registers a callback function (expense_category_selected) to handle the user's category selection.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /expense into the telegram bot.

