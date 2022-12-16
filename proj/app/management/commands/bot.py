import os
from django.core.management.base import BaseCommand
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from app.models import Message

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

bot = Bot(token='5817796122:AAEZaaFLlc8epYEUs4aULw-ImcmLPAxe9NI')
dp = Dispatcher(bot)


@dp.message_handler()
async def proceed_text_message(msg: types.Message):
    Message.objects.create(text=msg.text)
    await msg.answer('Message saved in database')


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        executor.start_polling(dp, skip_updates=True)
