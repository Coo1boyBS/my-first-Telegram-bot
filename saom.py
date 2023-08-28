#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
TOKEN = "6652299113:AAHCPzqqwci7kB3igG8_IP8RMh9xuu_9G1I"

from telebot.async_telebot import AsyncTeleBot
import wikipedia
bot = AsyncTeleBot(TOKEN)



# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    text = message.text
    natija = wikipedia.summary(text)
    await bot.reply_to(message, natija)


import asyncio
asyncio.run(bot.polling())