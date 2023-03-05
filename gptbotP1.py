import logging
from aiogram import Bot, Dispatcher, executor, types

# tokens
bot_Token = '<your botfather token>'

# log
logging.basicConfig(level=logging.INFO)

# init aiogram
bot = Bot(token=bot_Token)
dp = Dispatcher(bot)


@dp.message_handler()
async def start(message: types.Message):
    await message.answer(message.text)

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)