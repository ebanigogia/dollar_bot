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
    
    
    categories = helper.getSpendCategories()

    if categories:
        message = "List of Categories:\n"
        for category in categories:
            message += f"- {category}\n"
    else:
        message = "No categories available."
    bot.send_message(chat_id, message)