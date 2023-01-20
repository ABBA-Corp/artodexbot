from aiogram import types

from tgbot.db.dao.holder import HolderDao


async def order_history(
        message: types.Message,
        dao: HolderDao
):
    orders = await dao.order.get_all_orders()
    orders_list = []
    for index, order in enumerate(orders, start=1):
        orders_list.append(
            f"{index}. {order.name}\n"
        )
    await message.answer(
        text="".join(orders_list)
    )
