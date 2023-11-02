import os
import time
import io
from pathlib import Path

from aiogram import Router, types, F, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.methods import SendAudio
from aiogram.types import InputFile, FSInputFile

from keyboards.keyboards import menu
from methods import api_news
from aiogram.utils.chat_action import Bot

router = Router()
bot = Bot(token=os.getenv('BOT_TOKEN'))


class Search(StatesGroup):
    keyword_ = State()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer('Hi!', reply_markup=menu())


@router.message(F.text == 'Latest news')
async def latest_nees_handler(message: types.Message):
    messages = api_news.get_latest_news()
    await message.answer('10 latest information.')
    time.sleep(1)
    for news in messages:
        await message.answer_photo(photo=news['image'],
                                   caption='<b>' + news['title'] + '</b>' + '\n\n' +
                                           '<i>' + news['description'] + '</i>' + '\n\n' +
                                           'Url: ' + news['url'] + '\n\n' +
                                           'Author: ' + news['author'] + '©\n\n' +
                                           'Published: ' + news['published'][:19]
                                   )


@router.message(F.text == 'Search')
async def search_news_handler(messages: types.Message, state: FSMContext):
    await state.set_state(Search.keyword_)
    await messages.answer('Enter the information you want to search for!')


@router.message(Search.keyword_)
async def searched_news(message: types.Message, state: FSMContext):
    await state.update_data(keyword_=message.text)
    keyb = await state.get_data()
    await state.clear()

    try:
        new = api_news.get_search_news(keyb['keyword_'])
        for news in new:
            await message.answer_photo(photo=news['image'],
                                       caption='<b>' + news['title'] + '</b>' + '\n\n' +
                                               '<i>' + news['description'] + '</i>' + '\n\n' +
                                               'Url: ' + news['url'] + '\n\n' +
                                               'Author: ' + news['author'] + '©\n\n' +
                                               'Published: ' + news['published'][:19]
                                       )
    except Exception:
        await message.answer('Information has not detected')


@router.message(F.text == 'About us')
async def about_us_handler(message: types.Message):
    await message.answer('Author:@tolibov_asilbek.\nTeam with @RUSTAMJON_29_00™\n\nSeacher bot©')

# @router.message(F.text == 'About us')
# async def send_audio(message: types.Message):
#     await bot.send_audio(message.from_user.id, open("routers/music.mp3", "rb"))
