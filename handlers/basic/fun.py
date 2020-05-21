import re
from random import randint

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp

from utils.misc.random_num_generator import generate_num


@dp.message_handler(Command("gay", prefixes="!/"))
async def gay(message: types.Message):
    """Хедлер, для обработки комманды /gay или !gay

    В ответ, бот отправляет то, на сколько пользователь является геем

    Примеры:
        /gay
        /gay Vasya
        !gay
        !gay Vasya
    """
    # разбиваем сообщение на комманду и аргументы через регулярное выражение
    command_parse = re.compile(r"(!gay|/gay) ?(\w+)?")
    parsed = command_parse.match(message.text)
    target = parsed.group(2)
    percentage = randint(0, 100)

    # если пользователь не ввёл цель, он сам становится ею
    if not target:
        target = message.from_user.get_mention()

    # отправляем результат
    await message.reply(f"🏳️‍🌈 Похоже, что {target} гей на {percentage}%")


@dp.message_handler(Command("biba", prefixes="!/"))
async def biba(message: types.Message):
    """Хедлер, для обработки комманды /biba или !biba

    В ответ, бот отправляет размер бибы

    Примеры:
        /biba
        /biba 10
        /biba 1-10
        /biba 10-1
        !biba
        !biba 10
        !biba 1-10
        !biba 10-1
    """
    # разбиваем сообщение на комманду и аргументы через регулярное выражение
    command_parse = re.compile(r"(!biba|/biba) ?(-?\d*)?-?(\d+)?")
    parsed = command_parse.match(message.text)
    # генерируем размер бибы от 1 до 30 по умолчанию (если аргументы не переданы)
    length = generate_num(parsed.group(2), parsed.group(3), 1, 30)

    # если это ответ на сообщение, будем берять бибу автора первичного сообщения
    # в противном случае, бибу того, кто использовал комманду
    if message.reply_to_message:
        target = message.reply_to_message.from_user.get_mention(as_html=True)
    else:
        target = message.from_user.get_mention(as_html=True)

    # отправляем
    await message.reply(f"🤤 У {target} биба {length}см")


@dp.message_handler(Command("roll", prefixes="!/"))
async def roll(message: types.Message):
    """Хедлер, для обработки комманды /roll или !roll

    В ответ, бот отправляет рандомное число

    Примеры:

        /roll
        /roll 10
        /roll 1-10
        /roll 10-1
        !roll
        !roll 10
        !roll 1-10
        !roll 10-1
    """
    # разбиваем сообщение на комманду и аргументы через регулярное выражение
    command_parse = re.compile(r"(!roll|/roll) ?(-?\d*)?-?(\d+)?")
    parsed = command_parse.match(message.text)
    # генерируем число
    num = generate_num(parsed.group(2), parsed.group(3))
    # отправляем число
    await message.reply(f"Ваше число: <b>{num}</b>")
