import telebot
import config
import logging
import time


#db_query = DbQuery()
bot = telebot.TeleBot(config.token)
logging.basicConfig(filename="sample.log", level=logging.INFO)

@bot.message_handler(regexp='/start')
def insert_into_a_db(message):
        bot.send_message(message.chat.id, "Добрый день. Предложите своё название проекта. Все сообщения — анонимны. Отправлять свои варианты можно неограниченное количество раз, они все будут записаны и учтены. ")
pass

@bot.message_handler(content_types='text')
def default_answer(message):
    bot.send_message(message.chat.id, "Большое спасибо, ваш вариант записан.")
    bot.send_message(164930191, message.text)
    pass

while True:
    # bot.polling(none_stop=True)
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.error(e)
        time.sleep(15)