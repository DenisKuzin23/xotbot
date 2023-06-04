from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from typing import List


class PlayField:
    
    def __init__(self):
        self._generate_battle_field()
        self._keyboard_markup = InlineKeyboardMarkup(inline_keyboard=self._generate_buttons())
        self._states_changed: List[str] = []
    
    def _generate_battle_field(self):
        self._battle_field = [['.', '.', '.'],
                              ['.', '.', '.'],
                              ['.', '.', '.']]

    def _generate_buttons(self):
        buttons = []
        for x in range(3):
            line = []
            for y in range(3):
                line.append(InlineKeyboardButton(text=self._battle_field[x][y], callback_data=f'{x + 1}{y + 1}'))
            buttons.append(line)
        return buttons    
    
    def get_battle_field(self) -> InlineKeyboardMarkup:
        return self._keyboard_markup
    
    def change_x_state(self, x: int, y: int) -> InlineKeyboardMarkup:
        return self._change_state(x, y, 'X')

    def change_o_state(self, x: int, y: int) -> InlineKeyboardMarkup:
        return self._change_state(x, y, 'O')

    def _change_state(self, x: int, y: int, symbol: str):
        sbtn = f'{x}{y}'
        if not sbtn in self._states_changed: 
            self._battle_field[x - 1][y - 1] = symbol
            self._keyboard_markup = InlineKeyboardMarkup(inline_keyboard=self._generate_buttons())
            self._states_changed.append(sbtn)
            return self._keyboard_markup
        else:
            return self._keyboard_markup

    def check_win(self) -> int:
        if len(self._states_changed) == 9:
            return 3
        if self._check_win_by('X'): return 1
        if self._check_win_by('O'): return 2
    
    def _check_win_by(self, sym: str) -> bool:
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

    def reset(self):
        self._generate_battle_field()
        self._keyboard_markup = InlineKeyboardMarkup(inline_keyboard=self._generate_buttons())
        self._states_changed = []
    