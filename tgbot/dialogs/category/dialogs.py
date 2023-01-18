import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import ScrollingGroup, Back, Select, Group, Cancel, Row, Button
from aiogram_dialog.widgets.text import Format

from .getters import categories_getter, products_getter, info_getter
from .handlers import on_category_clicked, on_product_clicked, on_buy_click
from ...states.states import MenuForm

menu = Dialog(
    Window(
        Format('{categories}'),
        Group(
            ScrollingGroup(
                Select(
                    text=Format('{item[0]}'),
                    id='categories',
                    item_id_getter=operator.itemgetter(1),
                    items='data',
                    on_click=on_category_clicked
                ),
                id='scrolling_categories',
                width=2,
                height=10
            ),
            Cancel(Format('{cancel}')),
        ),
        getter=categories_getter,
        state=MenuForm.category
    ),
    Window(
        Format('{products}'),
        Group(
            ScrollingGroup(
                Select(
                    text=Format('{item[0]}'),
                    id='products',
                    item_id_getter=operator.itemgetter(1),
                    items='data',
                    on_click=on_product_clicked
                ),
                id='scrolling_categories',
                width=2,
                height=10
            ),
            Cancel(Format('{cancel}')),
            Back(Format('{back}')),
        ),
        getter=products_getter,
        state=MenuForm.product
    ),
    Window(
        Format('{info}'),
        Button(
            Format('{buy}'),
            id='buy',
            on_click=on_buy_click
        ),
        Row(
            Cancel(Format('{cancel}')),
            Back(Format('{back}')),
        ),
        getter=info_getter,
        state=MenuForm.info
    ),
)
