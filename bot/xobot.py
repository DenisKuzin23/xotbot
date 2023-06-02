from aiogram import Bot, Dispatcher, types
from .config import TGID
from .play_field import PlayField
from typing import List, Tuple, Coroutine

bot = Bot(token=TGID)
dp = Dispatcher(bot)

users: List[Tuple[int, Coroutine]] = []
move = -1
pf = PlayField()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global move
    if len(users) < 1:
        msg = await bot.send_message(message.from_user.id, 'Игра крестики-нолики, ждем второго игрока')
        users.append((message.from_user.id, msg))
    else:
        await users[0][1].edit_text('Игра крестики-нолики, играем Х, ходим первыми')
        await users[0][1].edit_reply_markup(pf.get_battle_field())
        msg = await bot.send_message(message.from_user.id, 'Игра крестики-нолики, играем О, ходим вторыми', reply_markup=pf.get_battle_field())
        users.append((message.from_user.id, msg))
        move = 0


@dp.callback_query_handler(text='11')
async def btn11_clicked(query: types.CallbackQuery):
    await move_done(query, 1, 1)

@dp.callback_query_handler(text='12')
async def btn12_clicked(query: types.CallbackQuery):
    await move_done(query, 1, 2)


@dp.callback_query_handler(text='13')
async def btn13_clicked(query: types.CallbackQuery):
    await move_done(query, 1, 3)
    
@dp.callback_query_handler(text='21')
async def btn21_clicked(query: types.CallbackQuery):
    await move_done(query, 2, 1)

@dp.callback_query_handler(text='22')
async def btn22_clicked(query: types.CallbackQuery):
    await move_done(query, 2, 2)

@dp.callback_query_handler(text='23')
async def btn23_clicked(query: types.CallbackQuery):
    await move_done(query, 2, 3)

@dp.callback_query_handler(text='31')
async def btn31_clicked(query: types.CallbackQuery):
    await move_done(query, 3, 1)

@dp.callback_query_handler(text='32')
async def btn32_clicked(query: types.CallbackQuery):
    await move_done(query, 3, 2)

@dp.callback_query_handler(text='33')
async def btn33_clicked(query: types.CallbackQuery):
    await move_done(query, 3, 3)

async def move_done(query: types.CallbackQuery, x: int, y: int):
    global move
    if (query.from_user.id == users[0][0]) and move == 0:
        await users[0][1].edit_reply_markup(pf.change_x_state(x, y))
        await users[1][1].edit_reply_markup(pf.change_x_state(x, y))
        move = 1
    if (query.from_user.id == users[1][0]) and move == 1:
        await users[0][1].edit_reply_markup(pf.change_o_state(x, y))
        await users[1][1].edit_reply_markup(pf.change_o_state(x, y))
        move = 0
