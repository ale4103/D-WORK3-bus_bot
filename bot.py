import time
import telebot
import scrap
import config
#from telebot import apihelper
#from telebot import types

#apihelper.proxy = {'https': 'socks5://login:pass@12.11.22.33:8000'}

# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(config.TOKEN)


def split(a):
    b=a[0]
    b = str(str(b[0]) + ' - ' + str(b[1])[1:-1])
    try:
        c=a[1]
        c = str(str(c[0]) + ' - ' + str(c[1])[1:-1])
    except:
        c = 'no more buses'
    return(b,c)


# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(content_types=['text'])
def echo(message):

	#message.text = 'Kirovskiy z-d'
	#a = scrap.run(message.text)
	
    types = telebot.types
    markup = types.ReplyKeyboardMarkup()
    markup.row('Kirovskiy z-d')
    markup.row('Gorelovo -> R-V', 'Gorelovo -> SPb')
    markup.row('R-V -> Ropsha', 'R-V -> SPb')
    markup.row('Ropsha')
    print(message.text)
    a = scrap.run(message.text)
    print(a)
    
    b, c = split(a)



 
    bot.send_message(message.chat.id, b, reply_markup=markup)
    if c != 'no more buses':
        bot.send_message(message.chat.id, c, reply_markup=markup)
    # if d != 'no more buses':
    #     bot.send_message(message.chat.id, d, reply_markup=markup)
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, "Выбери остановку:", reply_markup=markup)
    #bot.send_message(message.chat.id, message.text)
    
    if message.text == '481':
        print(message.text)
	
    
    
    
    #Remove keyboard
    #hide_markup = telebot.types.ReplyKeyboardRemove()
    #bot.send_message(message.from_user.id, "Hide text:", reply_markup=hide_markup)

'''# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass
'''


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(10)
        except KeyboardInterrupt:
            print('interrupted!')
