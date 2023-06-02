from aiogram import Bot, Dispatcher, types
from .config import TGID
from .play_field import PlayField
from typing import List, Tuple, Coroutine

bot = Bot(token=TGID)
dp = Dispatcher(bot)

users: List[Tuple[int, Coroutine]] = []
pf = PlayField()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if len(users) < 1:
        msg = await bot.send_message(message.from_user.id, 'Игра крестики-нолики, ждем второго игрока')
        users.append((message.from_user.id, msg))
    else:
        await users[0][1].edit_text('Игра крестики-нолики, играем Х, ходим первыми')
        await users[0][1].edit_reply_markup(pf.get_battle_field())
        msg = await bot.send_message(message.from_user.id, 'Игра крестики-нолики, играем О, ходим вторыми', reply_markup=pf.get_battle_field())
        users.append((message.from_user.id, msg))


@dp.callback_query_handler(text='11')
async def btn11_clicked(query: types.CallbackQuery):
    if query.from_user.id == users[0][0]:
        await users[0][1].edit_reply_markup(pf.change_x_state(1, 1))
        await users[1][1].edit_reply_markup(pf.change_x_state(1, 1))
    else:
        await users[0][1].edit_reply_markup(pf.change_o_state(1, 1))
        await users[1][1].edit_reply_markup(pf.change_o_state(1, 1))

@dp.callback_query_handler(text='12')
async def btn11_clicked(query: types.CallbackQuery):
    if query.from_user.id == users[0][0]:
        await users[0][1].edit_reply_markup(pf.change_x_state(1, 2))
        await users[1][1].edit_reply_markup(pf.change_x_state(1, 2))
    else:
        await users[0][1].edit_reply_markup(pf.change_o_state(1, 2))
        await users[1][1].edit_reply_markup(pf.change_o_state(1, 2))


@dp.callback_query_handler(text='13')
async def btn11_clicked(query: types.CallbackQuery):
    if query.from_user.id == users[0][0]:
        await users[0][1].edit_reply_markup(pf.change_x_state(1, 3))
        await users[1][1].edit_reply_markup(pf.change_x_state(1, 3))
    else:
        await users[0][1].edit_reply_markup(pf.change_o_state(1, 3))
        await users[1][1].edit_reply_markup(pf.change_o_state(1, 3))
    
@dp.callback_query_handler(text='21')
async def btn11_clicked(query: types.CallbackQuery):
    if query.from_user.id == users[0][0]:
        await users[0][1].edit_reply_markup(pf.change_x_state(2, 1))
        await users[1][1].edit_reply_markup(pf.change_x_state(2, 1))
    else:
        await users[0][1].edit_reply_markup(pf.change_o_state(2, 1))
        await users[1][1].edit_reply_markup(pf.change_o_state(2, 1))

@dp.callback_query_handler(text='22')
async def btn11_clicked(query: types.CallbackQuery):
    if query.from_user.id == users[0][0]:
        await users[0][1].edit_reply_markup(pf.change_x_state(2, 2))
        await users[1][1].edit_reply_markup(pf.change_x_state(2, 2))
    else:
        await users[0][1].edit_reply_markup(pf.change_o_state(2, 2))
        await users[1][1].edit_reply_markup(pf.change_o_state(2, 2))


@dp.callback_query_handler(text='23')
async def btn11_clicked(query: types.CallbackQuery):
    if query.from_user.id == users[0][0]:
        await users[0][1].edit_reply_markup(pf.change_x_state(2, 3))
        await users[1][1].edit_reply_markup(pf.change_x_state(2, 3))
    else:
        await users[0][1].edit_reply_markup(pf.change_o_state(2, 3))
        await users[1][1].edit_reply_markup(pf.change_o_state(2, 3))

@dp.callback_query_handler(text='31')
async def btn11_clicked(query: types.CallbackQuery):
    if query.from_user.id == users[0][0]:
        await users[0][1].edit_reply_markup(pf.change_x_state(3, 1))
        await users[1][1].edit_reply_markup(pf.change_x_state(3, 1))
    else:
        await users[0][1].edit_reply_markup(pf.change_o_state(3, 1))
        await users[1][1].edit_reply_markup(pf.change_o_state(3, 1))

@dp.callback_query_handler(text='32')
async def btn11_clicked(query: types.CallbackQuery):
    if query.from_user.id == users[0][0]:
        await users[0][1].edit_reply_markup(pf.change_x_state(3, 2))
        await users[1][1].edit_reply_markup(pf.change_x_state(3, 2))
    else:
        await users[0][1].edit_reply_markup(pf.change_o_state(3, 2))
        await users[1][1].edit_reply_markup(pf.change_o_state(3, 2))


@dp.callback_query_handler(text='33')
async def btn11_clicked(query: types.CallbackQuery):
    if query.from_user.id == users[0][0]:
        await users[0][1].edit_reply_markup(pf.change_x_state(3, 3))
        await users[1][1].edit_reply_markup(pf.change_x_state(3, 3))
    else:
        await users[0][1].edit_reply_markup(pf.change_o_state(3, 3))
        await users[1][1].edit_reply_markup(pf.change_o_state(3, 3))
