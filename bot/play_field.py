from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from typing import List


class PlayField: # класс, реализующий логику игрового поля
    
    def __init__(self):
        self._generate_battle_field() # вызов метода генерации игрового поля
        self._keyboard_markup = InlineKeyboardMarkup(inline_keyboard=self._generate_buttons()) #клавиатру в телеграм боте, представляющая собой 3 радя по 3 кнопки
        self._states_changed: List[str] = [] #список заполненных клеток
    
    def _generate_battle_field(self):
        self._battle_field = [['.', '.', '.'], #заполнение массива игрового поля точками
                              ['.', '.', '.'],
                              ['.', '.', '.']]

    def _generate_buttons(self): #генерация кнопок игрового поля, которые будут отображаться пользователям
        buttons = []
        for x in range(3):
            line = []
            for y in range(3):
                line.append(InlineKeyboardButton(text=self._battle_field[x][y], callback_data=f'{x + 1}{y + 1}'))#создается кнопка с содержимым (пусто, Х или О), а так-же передается координата кнопки
            buttons.append(line)
        return buttons    
    
    def get_battle_field(self) -> InlineKeyboardMarkup: # возврат кнопок игрового поля, для отображения пользователю
        return self._keyboard_markup
    
    def change_x_state(self, x: int, y: int) -> InlineKeyboardMarkup:
        return self._change_state(x, y, 'X') #меняется статус клетки игрового поля на Х

    def change_o_state(self, x: int, y: int) -> InlineKeyboardMarkup:
        return self._change_state(x, y, 'O') #меняется статус клетки игрового поля на О

    def _change_state(self, x: int, y: int, symbol: str):
        sbtn = f'{x}{y}'
        if not sbtn in self._states_changed: #проверяем, заполнено ли уже данная клетка или еще нет
            self._battle_field[x - 1][y - 1] = symbol #если не заполнена, то менем содержимое клетки на Х или О
            self._keyboard_markup = InlineKeyboardMarkup(inline_keyboard=self._generate_buttons()) #генерируем клавиатуру заново
            self._states_changed.append(sbtn) #помечаем клетку заполненной
            return self._keyboard_markup
        else:
            return self._keyboard_markup

    def check_win(self) -> int:
        if self._check_win_by('X'): return 1 #проверка победы Х
        if self._check_win_by('O'): return 2 #проверка победы О
        if len(self._states_changed) == 9: #если заполнены все 9 клеток, значит ничья
            return 3
    
    def _check_win_by(self, sym: str) -> bool: #метод, перебирающий все возможные выигрышные комбнации на поле, и возвращающий True если она есть
        bf = self._battle_field
        if ((bf[0][0] == sym and bf[0][1] == sym and bf[0][2] == sym) 
            or (bf[1][0] == sym and bf[1][1] == sym and bf[1][2] == sym)
            or (bf[2][0] == sym and bf[2][1] == sym and bf[2][2] == sym)
            or (bf[0][0] == sym and bf[1][0] == sym and bf[2][0] == sym)
            or (bf[0][1] == sym and bf[1][1] == sym and bf[2][1] == sym)
            or (bf[0][2] == sym and bf[1][2] == sym and bf[2][2] == sym)
            or (bf[0][0] == sym and bf[1][1] == sym and bf[2][2] == sym)
            or (bf[0][2] == sym and bf[1][1] == sym and bf[2][0] == sym)):
                return True

    def reset(self): #сброс состояния на начало новой игры
        self._generate_battle_field() #генерация пустого игрового поля
        self._keyboard_markup = InlineKeyboardMarkup(inline_keyboard=self._generate_buttons()) #создание клавиатуры, для отображения пользователю
        self._states_changed = [] #обнуление всех занятых клеток
    