# states.py
from aiogram.fsm.state import State, StatesGroup

class BirthdayState(StatesGroup):
    waiting_for_name = State()
    waiting_for_date = State()

class EditBirthdayState(StatesGroup):
    waiting_for_new_name = State()
    waiting_for_new_date = State()s