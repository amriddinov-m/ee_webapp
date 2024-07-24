import asyncio
import logging
import os
import sys

import django
from aiogram import Bot


def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "ee_webapp.settings"
    )
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    django.setup()


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    from bot.handlers import dp
    bot = Bot(token='7234642585:AAFYhvaBJHFYnQ14O2lqlqegDQIwl7SoW_g')
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == '__main__':
    setup_django()

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
