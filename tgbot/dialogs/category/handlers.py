from aiogram import types
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.managed import ManagedWidgetAdapter

from tgbot.config import load_config
from tgbot.dto.constants import i18n
from tgbot.dto.models import Inventory
from tgbot.misc.api import get_products, get_product_info
from tgbot.states.states import MenuForm


_ = i18n.gettext


async def on_category_clicked(
        query: types.CallbackQuery,
        widget: ManagedWidgetAdapter,
        manager: DialogManager,
        item_id: str
):
    await manager.switch_to(MenuForm.product)
    manager.data.update(item_id=item_id)


async def on_product_clicked(
        query: types.CallbackQuery,
        widget: ManagedWidgetAdapter,
        manager: DialogManager,
        item_id: str
):
    items = await get_products()
    if not items.inventory:
        await query.answer(text='Нет товаров', show_alert=True)
    else:
        await manager.switch_to(MenuForm.info)
    manager.data.update(item_id=item_id, items=items)


async def on_buy_click(
        query: types.CallbackQuery,
        button: Button,
        manager: DialogManager
):
    config = load_config('bot.ini')
    item_id = manager.data.get('item_id')
    item = await get_product_info(code=item_id)
    info = _(
        "🗒 Наименование: {name}\n"
        "📤 Штрих-код: {barcode}"
    ).format(
        name=item.inventory[0].name,
        barcode=item.inventory[0].barcodes
    )
    await query.message.bot.send_message(
        chat_id=config.tg_bot.channel_id,
        text=info
    )
