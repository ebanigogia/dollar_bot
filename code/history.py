import helper
import logging
import csv
import io
from telebot import types

# === Documentation of history.py ===


def run(message, bot):
    """
    run(message, bot): This is the main function used to implement the delete feature.
    It takes 2 arguments for processing - message which is the message from the user, and bot which
    is the telegram bot object from the main code.py function. It calls helper.py to get the user's
    historical data and based on whether there is data available, it either prints an error message or
    displays the user's historical data.
    """
    try:
        helper.read_json()
        chat_id = message.chat.id
        user_history = helper.getUserHistory(chat_id)
        spend_total_str = ""
        if user_history is None:
            raise Exception("Sorry! No spending records found!")
        spend_total_str = "Here is your spending history : \nDATE, CATEGORY, AMOUNT,NOTES\n----------------------\n"
        if len(user_history) == 0:
            spend_total_str = "Sorry! No spending records found!"
        else:
            for rec in user_history:
                spend_total_str += str(rec) + "\n"
        bot.send_message(chat_id, spend_total_str)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oops!" + str(e))

def download_history(message,bot):
    
    try:
        chat_id = str(message.chat.id)
        user_list=helper.read_json()
        print(user_list)
        count = 0
        table = [["Date", "Category", "Amount in $","Notes"]]
        if chat_id not in list(user_list.keys()):
            raise Exception("Sorry! No spending records found!")
        if len(user_list[chat_id]["data"]) == 0:
            raise Exception("Sorry! No spending records found!")
        else:
            for date in user_list[chat_id]["data"]:
                date1,category,value,notes=date.split(",")
                table.append([date1,category,"$"+value,notes])
                count = count + 1
            if count == 0:
                raise Exception("Sorry! No spending records found!")

            s = io.StringIO()
            csv.writer(s).writerows(table)
            s.seek(0)
            buf = io.BytesIO()
            buf.write(s.getvalue().encode())
            buf.seek(0)
            buf.name = "history.csv"
            bot.send_document(chat_id, buf)

    except Exception as ex:
        logging.exception(str(ex), exc_info=True)
        bot.reply_to(message, str(ex))
