import GetWeather as parser
import BotConfig

URL0 = 'https://rp5.ru'
URL1 = '/Погода_в_мире'
URL = URL0 + URL1

from aiogram import Bot, Dispatcher, executor, types
bot = Bot(BotConfig.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


executor.start_polling(dp, skip_updates=True)

#countries_list, countries_links = parser.parse(URL) 
#print(countries_links)
