import helper
import logging
import telebot
from telebot import types
from datetime import datetime
import time
def run(message, bot):
    helper.read_json()
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    chat_id = message.chat.id
    """
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    for c in helper.getSpendCategories():
        markup.add(c)
        bot.reply_to(message, "Categories", reply_markup=markup)
        """
    
    categories = helper.getSpendCategories()

    if categories:
        message = "List of Categories:\n"
        for category in categories:
            message += f"- {category}\n"
    else:
        message = "No categories available."
    bot.send_message(chat_id, message)
    """
    try:
        print("here")
        chat_id = message.chat.id
        if helper.spend_categories(chat_id):
            display_categories(message, bot)
        else:
            raise Exception(
                "There are no categories available"
            )
    except Exception as e:
        helper.throw_exception(e, message, bot, logging)
        """
"""
def display_categories(message, bot):
    display_overall_budget(message, bot): It takes 2 arguments for processing -
    message which is the message from the user, and bot which is the telegram bot
    object from the run(message, bot): in the same file. It gets the budget for the
    user based on their chat ID using the helper module and returns the same through the bot to the Telegram UI.
    chat_id = message.chat.id
    for c in helper.getSpendCategories():
        markup.add(c)
    bot.send_message(chat_id, markup)
    """