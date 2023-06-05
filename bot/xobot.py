from aiogram import Bot, Dispatcher, types
from .config import TGID
from .play_field import PlayField
from typing import List, Tuple, Coroutine

bot = Bot(token=TGID) #создание бота, токен бота получается в тг у @botfather
dp = Dispatcher(bot) #создание обработчика событий бота

users: List[Tuple[int, Coroutine]] = [] #список игроков
move = -1 #инициализация переменной очереди хода
pf = PlayField() #создание экземпляра класса игрового поля

@dp.message_handler(commands=['start']) #обработка команды старт
async def start(message: types.Message):
    global move
    global users
    if len(users) < 1: #если подключается первый игрок, то выводим сообщение и ожидаем подключения второго игрока
        msg = await bot.send_message(message.from_user.id, 'Игра крестики-нолики, ждем второго игрока')
        users.append((message.from_user.id, msg))
    else:
        await users[0][1].edit_text('Игра крестики-нолики, играем Х, ходим первыми') #если подключился второй игрок, то выводим сообщения об очередности ходов
        await users[0][1].edit_reply_markup(pf.get_battle_field())
        msg = await bot.send_message(message.from_user.id, 'Игра крестики-нолики, играем О, ходим вторыми', reply_markup=pf.get_battle_field())
        users.append((message.from_user.id, msg))
        move = 0 #устанавливаем переменную очереди хода


@dp.callback_query_handler(text='11')#обработчик первой кнопки первого ряда
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
    global users
    if (query.from_user.id == users[0][0]) and move == 0:#если сходил первый игрок, то устанавливаем Х в клетку и обновляем игровое поля для всех игроков
        await users[0][1].edit_reply_markup(pf.change_x_state(x, y))#редактируем клавиатуру с новым содержимым игрового поля
        await users[1][1].edit_reply_markup(pf.change_x_state(x, y))
        move = 1
    if (query.from_user.id == users[1][0]) and move == 1:#если сходил первый игрок, то устанавливаем О в клетку и обновляем игровое поля для всех игроков
        await users[0][1].edit_reply_markup(pf.change_o_state(x, y))
        await users[1][1].edit_reply_markup(pf.change_o_state(x, y))
        move = 0
    if pf.check_win() == 1:#если выиграл первый игрок, то завершаем игру и рассылаем сообщения
        await users[0][1].edit_text('Вы выиграли!!!')
        await users[1][1].edit_text('Вы проиграли...')
        move = -1
        users = []
        pf.reset()
    elif pf.check_win() == 2:#если выиграл второй игрок, то завершаем игру и рассылаем сообщения
        await users[0][1].edit_text('Вы проиграли...')
        await users[1][1].edit_text('Вы выиграли!!!')
        move = -1
        users = []
        pf.reset()
    elif pf.check_win() == 3:#сюда мы попадаем, если ничья
        await users[0][1].edit_text('Ничья')
        await users[1][1].edit_text('Ничья')
        move = -1
        users = []
        pf.reset()