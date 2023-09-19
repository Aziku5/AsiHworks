from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (Message,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove,
                           KeyboardButton
                           )
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

dialogue_FSM_router = Router()


class UserData(StatesGroup):
    name = State()
    age = State()
    gender = State()


@dialogue_FSM_router.message(F.text == 'Отмена')
@dialogue_FSM_router.message(Command("cancel"))
async def cancel_dialogue_FSM(message: Message, state: FSMContext):
    await state.finish()
    await message.answer(text="Диалог окончен.", reply_markup=ReplyKeyboardRemove())


@dialogue_FSM_router.message(Command("ask"))
async def start_dialogue_FSM(message: Message, state: FSMContext):
    await state.set_state(UserData.name)
    await message.answer("Добро пожаловать! Заполните анкету.")
    await message.answer("Как тебя зовут?")


@dialogue_FSM_router.message(F.text, UserData.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(UserData.age)
    await message.answer("Сколько тебе лет?")


@dialogue_FSM_router.message(F.text.isdigit, UserData.age)
async def process_age(message: Message, state: FSMContext):
    age = int(message.text)
    if age < 0 or age > 100:
        await message.answer("Пожалуйста, введите реальный возраст.")
        return
    await state.update_data(age=age)
    await state.set_state(UserData.gender)
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Муж"), KeyboardButton(text="Жен")]
        ],
        resize_keyboard=True
    )
    await message.answer("Какой у тебя пол?", reply_markup=kb)


@dialogue_FSM_router.message(F.text, UserData.gender)
async def process_gender(message: Message, state: FSMContext):
    gender = message.text.lower()
    if gender not in ['муж', 'жен']:
        kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Муж"), KeyboardButton(text="Жен")]
            ],
            resize_keyboard=True
        )
        await message.answer(text="Пожалуйста, выбери пол с помощью кнопок.", reply_markup=kb)
        return
    await state.update_data(gender=gender)
    data = await state.get_data()
    await message.answer(f"Спасибо за заполнение анкеты!\n"
                         f"Имя: {data['name']}\n"
                         f"Возраст: {data['age']}\n"
                         f"Пол: {data['gender']}",
                         reply_markup=ReplyKeyboardRemove())
    await state.finish()
