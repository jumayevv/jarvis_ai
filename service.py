from cgitb import text
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
)
from sqlite3 import *
import info

bot = Bot(token=info.BotToken, parse_mode="markdown")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def Welcome(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,text=f"*Salom, men Boburjon tomonidan yaratilgan suniiy intellektman\nsizga qanday yordam bera olaman ?*")
 
@dp.message_handler(commands="021218")
async def GetPicture(message: types.Message):
        user_id = message.from_user.id
        photo = open('photo.jpg', 'rb')
        caption = f"""*021218⚡️\n*"""
        # gif jo'natish uchun bu funksiya ishlatiladi
        # gif_path = "ronaldo.gif"
        # await message.answer_document(document=open(gif_path, 'rb'), caption=caption,parse_mode=types.ParseMode.MARKDOWN)
        await message.answer_photo(photo, caption=caption, parse_mode=types.ParseMode.MARKDOWN)
        photo.close()

@dp.message_handler(text="limitni tekshirish")
async def GetDailyLimit(message: types.Message):
        limit=0
        await message.reply(
            f"*{info.call_man} Sizda yana {limit} ta kunlik so'rov qoldi*\n")

# run
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
