import logging
import openai
import asyncio

from aiogram import Bot, Dispatcher, executor, types

# tokens
bot_Token = '<your botfather token>'
openai_Token = '<your openai token>'

# log
logging.basicConfig(level=logging.INFO)

# init openai
openai.api_key = openai_Token

# init aiogram
bot = Bot(token=bot_Token)
dp = Dispatcher(bot)

# Create a dictionary to store previous messages and responses
prev_responses = {}

@dp.message_handler()
async def gpt_answer(message: types.Message):
    # check if the user has sent a previous message
    if message.chat.id in prev_responses:
        # if so, use the previous response as the prompt
        prev_prompt = str(prev_responses[message.chat.id])
        prompt = prev_prompt + " " + message.text
    else:
        # otherwise, use the user's message as the prompt
        prompt = message.text

    model_engine = "text-davinci-003"
    max_tokens = 1000 # default 1024
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Store the current message and response in the dictionary
    prev_responses[message.chat.id] = completion.choices[0].text

    await message.answer('ChatGPT is responding ... ')
    await message.answer(completion.choices[0].text)


# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
