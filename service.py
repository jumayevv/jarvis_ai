from cgitb import text
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from sqlite3 import *
import info
import details

bot = Bot(token=info.BotToken, parse_mode="markdown")
dp = Dispatcher(bot=bot)
database = details
# menu_btn = [[KeyboardButton("🔗button 1")],[KeyboardButton("⚡️button 2")]]
# menu = ReplyKeyboardMarkup(menu_btn, resize_keyboard=True)

@dp.message_handler(commands=["start"])
async def Welcome(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,text=f"*Salom, men Boburjon tomonidan yaratilgan suniiy intellektman\nsizga qanday yordam bera olaman ?*")

@dp.message_handler(commands=["setname"])
async def Welcome(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,text="*sizga nima deb murojat qilishimni xohlyasiz ?*")
    @dp.message_handler()
    async def getname(message : types.Message):
        user_id = message.from_user.id
        name = message.text
        details.AddUser(user_id,name)
        await bot.send_message(chat_id=message.from_user.id,text=f"*qabul qildim✅*")


@dp.message_handler(commands="021218")
async def GetPicture(message: types.Message):
        photo = open('photo.jpg', 'rb')
        caption = f"""*021218⚡️\n*"""
        # for sending gif
        # gif_path = "ronaldo.gif"
        # await message.answer_document(document=open(gif_path, 'rb'), caption=caption,parse_mode=types.ParseMode.MARKDOWN)
        await message.answer_photo(photo, caption=caption, parse_mode=types.ParseMode.MARKDOWN)
        photo.close()


@dp.message_handler(regexp=r'https?://(?:www\.)?instagram\.com/.+')
async def download_instagram_video(message: types.Message):

    video_link = message.text
    
## download video or picture from instagram section

@dp.message_handler(commands="about")
async def GetPicture(message: types.Message):
        user_name = database.GetUserName(message.from_user.id)
        user_id = message.from_user.id
        caption = f"""*J.A.R.V.I.S⚡️ -> Just A Rather Very Intelligent System\nthe most powerfull A.I in existance\n*"""
        await message.bot.send_message(chat_id=user_id,text=caption,parse_mode=types.ParseMode.MARKDOWN)
        await message.bot.send_message(chat_id=user_id,text=f"*\nsizga yana qanday yordam bera olaman {user_name}? \n*")

# @dp.message_handler(text="limitni tekshirish")
# async def GetDailyLimit(message: types.Message):
#         limit=0
#         await message.reply(
#             f"*{info.call_man} Sizda yana {limit} ta kunlik so'rov qoldi*\n")

# run
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
