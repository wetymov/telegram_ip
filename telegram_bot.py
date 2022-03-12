import telebot 
import requests
from pyfiglet import Figlet
token = 'token'

bot = telebot.TeleBot(token)


def get_info_by_ip(ip='127.0.0.1'):
    try:
        
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]' : response.get('query'),
            '[Country]' : response.get('country'),
            '[City]' : response.get('city'),
            '[Lat]' : response.get('lat'),
            '[Lon]' : response.get('lon')
        }
        return data
    except requests.exceptions.ConnectionError:
        bot.send_message(message.chat.id, f'Вы не правильно ввели айпи')


@bot.message_handler(content_types='text')
def ip_start(message):
    prewi_text = Figlet(font='digital')
    intq = prewi_text.renderText('IP INFO')
    bot.send_message(message.chat.id, f'{intq}')
    n = get_info_by_ip(message.text)
    for k,v in n.items():
        bot.send_message(message.chat.id, f'{k} : {v}')


bot.polling(none_stop=True)
