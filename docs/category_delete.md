# About MyDollarBot's /expense Feature
This feature enables the user to delete the category from the list.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/ebanigogia/dollar_bot/blob/main/code/category_delete.py)

# Code Description
## Functions

1. run:
This function is called when the user initiates the process of deleting a spending category. It does the following:
Calls helper.read_json(), presumably to read data from a JSON file that may contain information about spending categories.
Retrieves the chat_id from the message object, which is necessary to know where to send responses.
Sends a message to the user, asking them which category they want to delete.
Registers a "next step handler," which will be deletion, to handle the user's response. It also passes the bot object as an argument to the next step handler.

2. deletion:
This function is called after the user provides the category they want to delete. It performs the following tasks:
Creates a one-time reply keyboard markup.
Retrieves the chat_id from the message object.
Retrieves the category to be removed from the user's message.
Converts the user's input to lowercase and compares it with lowercase versions of categories obtained from helper.getSpendCategories().
If the category to remove is found in the list of categories, it asks the user for confirmation by sending a message with "Y/N" options.
If the category is not in the list, it informs the user that the category is not in the list.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /category and select delete from the given options.
