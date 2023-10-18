import helper
import logging
import telebot
from telebot import types
from datetime import datetime
def run(message, bot):
    helper.read_json()
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    m = bot.send_message(chat_id, "Do you want to add a new category? Y/N")
    bot.register_next_step_handler(m, post_user_def_category, bot)

def post_user_def_category(message, bot):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    chat_id = message.chat.id
    if str(message.text) == "Y" or str(message.text) == "y":
        message1 = bot.send_message(chat_id, "Please enter your category")
        bot.register_next_step_handler(message1, post_append_spend, bot)

def post_append_spend(message, bot):

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    selected_category = message.text
    chat_id = message.chat.id
    lowercase_user_input = selected_category.lower()
    lowercase_categories = [category.lower() for category in helper.getSpendCategories()]
    """
    helper.spend_categories.append(selected_category)
    """
    if lowercase_user_input not in lowercase_categories:
        helper.spend_categories.append(selected_category)
        bot.send_message(chat_id, f"'{selected_category}' has been added to the list.")
    else:
        bot.send_message(chat_id, f"'{selected_category}' is already in the list and won't be added.")