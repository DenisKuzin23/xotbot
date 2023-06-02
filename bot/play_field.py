from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from typing import List


class PlayField:
    
    def __init__(self):
        self._buttons = [[InlineKeyboardButton(text='.', callback_data='11'), InlineKeyboardButton(text='.', callback_data='12'), InlineKeyboardButton(text='.', callback_data='13')],
                   [InlineKeyboardButton(text='.', callback_data='21'), InlineKeyboardButton(text='.', callback_data='22'), InlineKeyboardButton(text='.', callback_data='23')],
                   [InlineKeyboardButton(text='.', callback_data='31'), InlineKeyboardButton(text='.', callback_data='32'), InlineKeyboardButton(text='.', callback_data='33')]]
        self._keyboard_markup = InlineKeyboardMarkup(inline_keyboard=self._buttons)
        self._states_changed: List[str] = []
    
    def get_battle_field(self) -> InlineKeyboardMarkup:
        return self._keyboard_markup
    
    def change_x_state(self, x: int, y: int) -> InlineKeyboardMarkup:
        return self._change_state(x, y, 'X')

    def change_o_state(self, x: int, y: int) -> InlineKeyboardMarkup:
        return self._change_state(x, y, 'O')

    def _change_state(self, x: int, y: int, symbol: str):
        sbtn = f'{x}{y}'
        if not sbtn in self._states_changed: 
            self._buttons[x - 1][y - 1] = InlineKeyboardButton(text=symbol, callback_data=sbtn)
            self._keyboard_markup = InlineKeyboardMarkup(inline_keyboard=self._buttons)
            self._states_changed.append(sbtn)
            return self._keyboard_markup
        else:
            return self._keyboard_markup
