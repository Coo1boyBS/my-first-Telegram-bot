import logging
import wikipedia
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

# Set your Telegram API token here
API_TOKEN = '6652299113:AAHCPzqqwci7kB3igG8_IP8RMh9xuu_9G1I'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

# Wikipedia language
wikipedia.set_lang("ru")  # You can change this to a different language

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to the Wikipedia Bot! Send me the title of the article you want to know about.")

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def search_wikipedia(message: types.Message):
    try:
        article_title = message.text
        summary = wikipedia.summary(article_title)
        await message.reply(summary)
    except wikipedia.exceptions.PageError:
        await message.reply("Sorry, the article was not found.")
    except wikipedia.exceptions.DisambiguationError as e:
        await message.reply("The search term is ambiguous. Please be more specific.")
    except Exception as e:
        await message.reply("An error occurred while processing your request.")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
