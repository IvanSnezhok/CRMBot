from aiogram.dispatcher.filters.state import State, StatesGroup


class CheckList1(StatesGroup):
    cl1 = State()
    ccl1 = State()


class CheckList2(StatesGroup):
    cl2 = State()
    ccl2 = State()


class LitniyMaydanchik1(StatesGroup):
    lm1 = State()
    clm1 = State()


class LitniyMaydanchik2(StatesGroup):
    lm2 = State()
    clm2 = State()
