from aiogram.dispatcher.filters.state import StatesGroup, State


class UserMessageState(StatesGroup):
    answer_text = State()
    # film_id = State()
    # film_text = State()
