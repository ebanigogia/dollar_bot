import helper
import logging
import telebot
from telebot import types
from datetime import datetime
import time

def run(message, bot):
    helper.read_json()
    chat_id = message.chat.id
    m=bot.send_message(chat_id, "Which Category you want to Delete")
    bot.register_next_step_handler(m, deletion, bot)

def deletion(message,bot):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    chat_id = message.chat.id
    category_to_remove = message.text
    lowercase_user_input = category_to_remove.lower()
    lowercase_categories = [category.lower() for category in helper.getSpendCategories()]
    if lowercase_user_input in lowercase_categories:
        message=bot.send_message(chat_id, "Are you sure you want to delete this category? Y/N ")
        bot.register_next_step_handler(message, confirm_deletion,bot,category_to_remove)
    else:
        bot.send_message(chat_id, f"'{category_to_remove}' Category is not in the list.")

def confirm_deletion(message,bot,category_to_remove):
    chat_id = message.chat.id
    response = message.text.lower()

    if response == "y":
        """
        category_to_remove = message.text
        """
        # Perform the deletion logic here
        if category_to_remove in helper.getSpendCategories():
            helper.getSpendCategories().remove(category_to_remove)
            bot.send_message(chat_id, f"'{category_to_remove}' has been removed from the list")
        else:
            bot.send_message(chat_id, f"'{category_to_remove}' was not found in the list.")
    elif response == "n":
        bot.send_message(chat_id, "Deletion canceled.")
    else:
        bot.send_message(chat_id, "Invalid response. Please enter 'Y' or 'N'.")

    """
        response = message.text
        if response.lower() == "y":
            helper.getSpendCategories.remove(category_to_remove)
            bot.send_message(chat_id, f"'{category_to_remove}' has been removed from the list")
        elif response.lower() == "n":
            bot.send_message(chat_id, "Deletion canceled.")
    else:
        bot.send_message(chat_id, f"'{category_to_remove}' Category is not in the list.")

if __name__ == "__main__":
    bot.polling()
    """
    