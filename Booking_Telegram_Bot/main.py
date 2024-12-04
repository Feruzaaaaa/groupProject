import telebot
from telebot import types
from random import choice


bot = telebot.TeleBot('7607040571:AAEtWBhazqlKXlXIxrjGN1S-uEWHntcEjCM')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Book Classroom", callback_data="bookClassroom")
    btn2 = types.InlineKeyboardButton("Current Schedule", callback_data="currentSchedule")
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, f"""Welcome to the Classroom Booking Bot! 📚✨

Here’s what you can do:
- View the current classroom schedule.
- Book a classroom for your desired time.
- Receive booking confirmations once approved by the admin.

Available Commands:
- /schedule – Check the current schedule of classrooms.
- /book – Start a new booking request.
- /help – Get assistance on how to use the bot.

🔔 Note: Your booking will need admin approval. You’ll receive a confirmation once it’s approved.

Let’s make classroom management easier! Start by typing /schedule or /book.""", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    url = 'https://www.ucentralasia.org/'
    markup = types.InlineKeyboardMarkup()
    website_btn = types.InlineKeyboardButton("Website", url=url)
    admin_btn = types.InlineKeyboardButton("Admin", url="https://t.me/kkwor")
    markup.row(website_btn, admin_btn)
    bot.send_message(message.chat.id, f"We are students from <b>University of Central Asia</b>, "
                                      f"and we created this bot to help other students to "
                                      f"<u>book classrooms</u> and check <u>current schedule</u>!\n\n"
                                      f"Please press <u>website</u> to check about UCA!\n"
                                      f"And if you are facing problems "
                                      f"or question regarding our bot, please reach out to <u>Admin</u>", reply_markup=markup, parse_mode='html')




@bot.message_handler(commands=['schedule'])
def schedule(message):
    bot.send_message(message.chat.id, "Here is the current schedule:\n\n\n\n.")


@bot.message_handler(commands=['book'])
def book(message):
    bot.send_message(message.chat.id, "Here is how to book:\n\n\n\n.")





@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "bookClassroom":
        bot.send_message(call.message.chat.id, "Sorry I am not smart enough to help you!")
    elif call.data == "currentSchedule":
        bot.send_message(call.message.chat.id, "Here is the current schedule:\n\n\n\n.")

@bot.message_handler()
def info(message):
    if message.text.lower() == "hello":
        bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}\nHow can I help you?")
    else:
        bot.send_message(message.chat.id, f"Sorry I don't your command \n<em>{message.text}</em>")
bot.polling(non_stop=True)