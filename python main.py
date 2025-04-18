import logging from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '8018333237:AAEOtrHWa-1hrcvRn4PteK_20laSfhg_IFU'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN) dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) async def send_welcome(message: types.Message): await message.reply("স্বাগতম JokarSojibAviatorBot-এ! আপনার Aviator গেম সহায়তা পেতে রেডি থাকুন।")

@dp.message_handler(commands=['help']) async def help_command(message: types.Message): await message.reply("সহায়তা কমান্ডসমূহ: /start - শুরু করুন /signal - গেম সিগন্যাল /stats - পরিসংখ্যান /vip - VIP তথ্য")

@dp.message_handler(commands=['vip']) async def vip_info(message: types.Message): await message.reply("VIP হবার জন্য আমাদের সাথে যোগাযোগ করুন: @CEO_JOKAR")

@dp.message_handler(commands=['signal']) async def signal_command(message: types.Message): await message.reply("আজকের গেম সিগন্যাল: 2x-3x Safe Mode")

@dp.message_handler(commands=['stats']) async def stats_command(message: types.Message): await message.reply("গেম পরিসংখ্যান এখনো সেটআপ চলছে...")

if name == 'main': executor.start_polling(dp, skip_updates=True)

