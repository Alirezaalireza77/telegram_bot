from aiogram import Bot, Dispatcher, types
import requests as rq
import os

bot = Bot('Token API')
dp = Dispatcher(bot)


@dp.message_reaction(command=["start"])
async def welcome(pm: types.message):
    pm.answer("enter your link please...")


@dp.message_reaction()
async def welcome(pm: types.message):
    dl = pm.text
    response = rq.get(dl)
    file_name = response.url.rfind["/"+1:]
    with open("file_name", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    pm.answer("your file is downloading...")

    await bot.send_document(
        chat_id=pm.from_user.id,
        document=open(file_name, 'rb')
    )
    os.remove(file_name)

if __name__ == "__main__":
    executor.start_polling(dp)
