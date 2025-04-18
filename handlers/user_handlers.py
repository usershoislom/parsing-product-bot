import uuid
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from lexicon.lexicon import texts
from services.process_excel import process_excel_file_data
from config.logger import logger

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    logger.info(f"user-{message.from_user.id} started bot")
    await message.answer(text=texts.get("start_message"))


@router.message(F.document)
async def process_excel_file(message: Message):
    logger.info(f"user-{message.from_user.id} sent document")
    document = message.document

    if document.mime_type in [
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/vnd.ms-excel",
    ]:
        file = await message.bot.get_file(document.file_id)
        file_name = f"downloads/{str(uuid.uuid4())[:8]}_{document.file_name}"
        await message.bot.download_file(file.file_path, destination=file_name)
        await message.answer(text=texts.get("processing_document"))

        async for title, url, price in process_excel_file_data(file_name, message):
            message_text = f"Название: {title}\nСсылка: {url}\nЦена: {price}"
            await message.answer(message_text)
    else:
        await message.answer(text=texts.get("send_document"))


@router.message()
async def process_any_other_command(message: Message):
    await message.answer("Нет такой команды! Нажмите /start")
