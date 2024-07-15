import telebot
from speechkit import text_to_speech
bot = telebot.TeleBot(" ")
MAX_SYMB = 500
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Добро пожаловать в бота, который озвучивает текст!Чтобы озвучить текст,используй команду /tts")
@bot.message_handler(commands=['tts'])
def tts1(message):
    bot.send_message(message.chat.id, "Введи текст (не более {} символов):".format(MAX_SYMB))

    def tts2(message):
        if len(message.text) > MAX_SYMB:
            bot.send_message(message.chat.id,
                             "Превышен лимит символов. Введите текст не более {} символов.".format(MAX_SYMB))
            bot.register_next_step_handler(message, tts2)  # Продолжаем ожидание корректного ввода
        else:
            text = message.text
            success, response = text_to_speech(text)

            if success:
                bot.send_voice(message.chat.id, response)
            else:
                bot.send_message(message.chat.id, "Ошибка")

    bot.register_next_step_handler(message, tts2)


bot.polling()
