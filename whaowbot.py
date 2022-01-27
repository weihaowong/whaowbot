import os
import telebot
from telebot import types
$heroku buildpacks:set heroku/php
$heroku create whaowbot --buildpack heroku/python

bot = telebot.TeleBot("5265129190:AAGZwDaoagX3VW_RzeS0YP_IALKt0_sqPXA",parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(message, 
  """Hi there. I am one of the most useless bot in Telegram!
/help""")

@bot.message_handler(commands=['help'])
def help(message):
  bot.send_message(message.chat.id, """
Commands menu

/image - Just use it 
/manytabs - Too many web.telegram.org tabs and this is what happens
/sound - The most harmony notification sound
/test - You would love it
/emoji - Emoji
/vid - Video message!
/sticker - Your favourite plane
  
This is a bot for testing. Get out of the way! """)

@bot.message_handler(commands=['spoiler'])
def spoiler(message):
  bot.send_message(message.chat.id, '||You are ugly||')


@bot.message_handler(commands=['sound'])
def music(message):
  bot.send_audio(message.chat.id, 'https://github.com/zhukov/webogram/blob/master/app/img/sound_a.mp3?raw=true', caption='Notification sound',title='notification.mp3' )


@bot.message_handler(commands=['image'])
def image(message):
  bot.send_photo(message.chat.id, 'https://raw.githubusercontent.com/zhukov/webogram/master/app/img/blank.gif', 'The tiniest image in the world?')

@bot.message_handler(commands=['manytabs'])
def manytabs(message):
  bot.send_photo(message.chat.id, 'https://github.com/zhukov/webogram/blob/master/app/img/Manytabs_2x.png?raw=true')

@bot.message_handler(commands=['test'])
def test(message):
  bot.send_video(message.chat.id,'https://media.giphy.com/media/Ju7l5y9osyymQ/giphy.gif', caption='Enjoy!')

@bot.message_handler(commands=['vid'])
def vid(message):
  bot.send_video_note(message.chat.id, 'DQACAgEAAxkBAAIBcmHyG-1uLHomXuBTBNsBvgRDDz5IAAJ2AAPsevBEBHEW-l5xRFojBA')

@bot.message_handler(commands=['sticker'])
def sticker(message):
  bot.send_sticker(message.chat.id, 'CAACAgUAAxkBAAIBQ2Hw8zv4WqgHl0kCAQvB3Dh55i_KAAI1BAACc2KIVzjAdT_8N0zZIwQ')


@bot.message_handler(commands=['emoji'])
def emoji(message):
  bot.send_photo(message.chat.id, 'https://lh3.googleusercontent.com/x6quxPOV6pZIfySisGMCJ4Uv1gKITV0LZ9_ZMrB_RdpUZQkV-Tp2cANrY04wTaqL4thg5hnNK2FE02ypuO9JVhLvmto4kY3tlmsTd7Q', "Not what you expected, eh?")

@bot.message_handler(content_types=['video_note'])
def hg(msg : types.Message):
    print(msg.video_note.file_id)

bot.infinity_polling()