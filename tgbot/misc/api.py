import json

from aiohttp import ClientSession, TCPConnector

from tgbot.dto.models import Categories, Inventory, InventoryItem


async def get_categories() -> Categories:
    # TODO base64 encode
    headers = {
        'Authorization': 'Basic YWRtaW5AYXJkb3RleDo1ODQ2Mg==',
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "code": "",
        "begin_created_on": "",
        "end_created_on": "",
        "begin_modified_on": "",
        "end_modified_on": ""
    })
    async with ClientSession(headers=headers, connector=TCPConnector(verify_ssl=False)) as session:
        async with session.post(url="https://smartup.online/b/anor/mxsx/mr/product_group$export", data=payload) as response:
            return Categories.parse_raw(await response.text())


async def get_products() -> Inventory:
    # TODO base64 encode
    headers = {
        'Authorization': 'Basic YWRtaW5AYXJkb3RleDo1ODQ2Mg==',
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "code": "",
        "begin_created_on": "",
        "end_created_on": "",
        "begin_modified_on": "",
        "end_modified_on": ""
    })
    async with ClientSession(headers=headers, connector=TCPConnector(verify_ssl=False)) as session:
        async with session.post(url="https://smartup.online/b/anor/mxsx/mr/inventory$export", data=payload) as response:
            return Inventory.parse_raw(await response.text())


async def get_product_info(code: str) -> Inventory:
    # TODO base64 encode
    headers = {
        'Authorization': 'Basic YWRtaW5AYXJkb3RleDo1ODQ2Mg==',
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "code": code,
        "begin_created_on": "",
        "end_created_on": "",
        "begin_modified_on": "",
        "end_modified_on": ""
    })
    async with ClientSession(headers=headers, connector=TCPConnector(verify_ssl=False)) as session:
        async with session.post(url="https://smartup.online/b/anor/mxsx/mr/inventory$export", data=payload) as response:
            return Inventory.parse_raw(await response.text())