from aiogram_dialog import DialogManager

from tgbot.dto.constants import i18n
from tgbot.misc.api import get_categories, get_products, get_product_info

_ = i18n.gettext


async def categories_getter(dialog_manager: DialogManager, **kwargs):
    categories_list = []
    categories = await get_categories()
    for product_group in categories.product_group:
        for product_type in product_group.product_group_types:
            categories_list.append((product_type.name, product_group.code))

    return {
        "categories": _('📦 Категории'),
        "data": categories_list,
        "cancel": _('🚫 Отмена')
    }


async def products_getter(dialog_manager: DialogManager, **kwargs):
    item_id = dialog_manager.data.get('item_id')
    item_list = []
    items = await get_products()
    for item in items.inventory:
        for group in item.groups:
            if group.group_code == item_id:
                item_list.append((item.name, item.code))
    return {
        "products": _('🚫 Отмена'),
        "data": item_list,
        "cancel": _('🚫 Отмена'),
        "back": _('⬅️ Назад')
    }


async def info_getter(dialog_manager: DialogManager, **kwargs):
    item_id = dialog_manager.current_context().dialog_data.get('item_id')
    item = await get_product_info(code=item_id)
    info = _(
        "🗒 Наименование: {name}\n"
        "📤 Штрих-код: {barcode}"
    ).format(
        name=item.inventory[0].name,
        barcode=item.inventory[0].barcodes
    )
    return {
        "info": info,
        "buy": _('💵 Купить'),
        "cancel": _('🚫 Отмена'),
        "back": _('⬅️ Назад')
    }
