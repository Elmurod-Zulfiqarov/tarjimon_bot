import logging

from aiogram import Bot, Dispatcher, executor, types
from gtranslate import get_translate

API_TOKEN = '5899866911:AAFoDkXPuKSBfzP6E_xnxvj4Y6qYCU1s_Hk'
admin = ['846140804']
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	await message.reply(f"Hello👋! {message.from_user.full_name} \nGoogletranslate botiga xush kelibsiz\nWelcome to the Googletranslate bot")
	admin_text = f"New User use from Translator Bot\nUser data:\nid - {message.from_user.id},\nfull_name - {message.from_user.full_name},\nusername - @{message.from_user.username},\nis_bot{message.from_user.is_bot},\nis_premium - {message.from_user.is_premium},\nlanguage_code - {message.from_user.language_code}, "
	await bot.send_message(admin[0], admin_text)


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
	text = "Bu bot sizga so'z va gaplarni\n🇺🇿O'zbek tilidan - 🏴󠁧󠁢󠁥󠁮󠁧󠁿Ingliz tiliga\n🏴󠁧󠁢󠁥󠁮󠁧󠁿Ingliz tilidan 🇺🇿O'zbek tiliga\n🏁boshqa tillardan - 🏴󠁧󠁢󠁥󠁮󠁧󠁿Ingliz tiliga tarjima qilib beradi!\nThis bot tells you words and phrases\nFrom Uzbek🇺🇿 to Englis🏴󠁧󠁢󠁥󠁮󠁧󠁿h\nFrom English🏴󠁧󠁢󠁥󠁮󠁧󠁿 to Uzbek🇺🇿\nfrom other languages🏁 ​​- will translate into English🏴󠁧󠁢󠁥󠁮󠁧󠁿!"
	await message.reply(text)


@dp.message_handler(commands=['admin'])
async def send_help(message: types.Message):
	text = "Bot haqida qo'shimcha savol va boshqa savollar yuzasidan admin bilan bog'lanishingiz mumkin\nadmin - @Elmurod_010409\nYou can contact the admin for additional questions about the bot and other questions\nadmin - @Elmurod_010409"
	await message.reply(text)


@dp.message_handler()
async def translator_bot(message: types.Message):
	respond = get_translate(message.text)
	await message.answer(respond)


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)