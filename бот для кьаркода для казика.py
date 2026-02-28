import telebot
import qrcode
qr = qrcode.QRCode()
bot = telebot.TeleBot("7856930650:AAFTM6vVVq3FM9XnzHWDGGEER1oBMDko9Kc")

@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    name_user = message.from_user.first_name
    text_user = message.text
    if text_user == "/start":
        bot.send_message(message.from_user.id,name_user+",здраствуйте это бот для qr кода")
    else:
        bot.send_message(message.from_user.id,"загружается qr-код.ожидайте")
    qr = qrcode.QRCode()
    qr.add_data(message.text)
    qr.make(fit=True)
    img = qr.make_image(back_color = "pink")
    img.save("img_qr_code.png")
    img_result = open ("img_qr_code.png","rb")
    bot.send_photo(message.from_user.id,img_result)

bot.polling(none_stop=True, interval=0)

