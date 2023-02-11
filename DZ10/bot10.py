import telebot

token = '5781228947:AAFznv9Ah9TTmht2eqguVdNVh5_wSfEmLHM'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.reply_to(message, "Привет. Я бот техподдержки. Введите команду /question, чтобы оставить свой вопрос")

@bot.message_handler(commands=['question'])
def prepare_to_question(message):
    bot.reply_to(message, 'Сформулируйте вопрос, я передам его оператору!')
    bot.register_next_step_handler(message, write_question)

def write_question(message):
    data = open ('question.txt', 'a', encoding='utf-8')
    data.write(f'{message.from_user.id}%%{message.from_user.first_name}{message.from_user.last_name}: {message.text}\n')
    data.close()
    bot.reply_to(message, 'Ваш вопрос направлен оператору! Время ожидания ответа - не более часа.')
    
#bot.infinity_polling()
bot.polling(none_stop=True)
