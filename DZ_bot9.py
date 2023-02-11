import random
import telebot, time
from telebot import types

game_started = False
r_number = None

token = 'Your_Token'
bot = telebot.TeleBot(token)

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('регистрация')
itembtn2 = types.KeyboardButton('оповещение')
itembtn3 = types.KeyboardButton('играть')
markup.add(itembtn1, itembtn2, itembtn3)
#bot.send_message(user.id, "Choose one letter:", reply_markup=markup)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.from_user.id, "Привет. Как дела?", reply_markup=markup)

@bot.message_handler(commands=['регистрация'])
def send_welcome(message):
	bot.reply_to(message, 'это команда "/регистрация" ')
 
@bot.message_handler(content_types=['text'])
def read_text_commands(message):
    global game_started
    global r_number
    
    data = open('message.txt', 'a', encoding='utf-8')
    text = f'{message.from_user.first_name} {message.from_user.last_name} {message.from_user.id}: {message.text}'
    data.writelines(f'{text}\n')
    data.close()
	#bot.reply_to(message, message.text)

    if game_started:
        if message.text.isdigit():
            number = int(message.text)
            if number > r_number:
                bot.reply_to(message, 'Нужно число меньше!') 
            elif number < r_number:
                bot.reply_to(message, 'Нужно число больше!')
            elif number == r_number:
                game_started = False
                bot.reply_to(message, 'Ура! Ты выиграл! Я загадал именно это число!')
            else:
                bot.reply_to(message, 'Ничего не понял....Попробуй еще раз!')
        else:
            bot.reply_to(message, 'Я ожидал твое число...!')
            return
        
    if message.text == 'регистрация':
        our_id = str(message.from_user.id)
        data = open('reg.txt', 'r', encoding = 'utf-8')
        registration_list = data.readlines()
        data.close()
        result = ''.join(registration_list)
        if our_id in result:
            bot.reply_to(message, 'Вы уже зарегистрированы!')
        else:
            data = open('reg.txt', 'a', encoding = 'utf-8')
            data.writelines(f'{our_id}\n')
            data.close()
            bot.reply_to(message, 'регистрация прошла успешно!')
    
    elif message.text == 'оповещение':
        data = open('reg.txt', 'r', encoding = 'utf-8')
        registration_list = data.readlines()
        data.close()
        #result = ''.join(registration_list)
        for id in registration_list:
            bot.send_message(id[:-1], 'Совещание через 5 минут!')
    
    elif message.text == 'играть':
        if not game_started:
            game_started= True
            r_number = random.randint(1, 1000)
            bot.reply_to(message, 'Я задумал число от 1 до 1000! Попробуй его отгадать!')
        else:
            bot.reply_to(message, 'Игра уже идет! Угадывай число!')
    
    elif message.text == 'вычислить':
        bot.reply_to(message, 'Введи выражение: ')
        bot.register_next_step_handler(message, calculate)
        
        
def calculate(message):
    try:
        bot.reply_to(message, f'Ответ: {eval(message.text)}')
    except Exception as e:
        bot.reply_to(message, f'Вы ввели неверное выражение')
    
#bot.polling(none_stop=True)    
#timeout=10, long_polling_timeout = 5
bot.infinity_polling()

