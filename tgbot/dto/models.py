from pydantic import BaseModel


class ProductGroupTypes(BaseModel):
    code: str | None
    name: str
    state: str
    order_no: str | None


class ProductGroup(BaseModel):
    code: str | None
    name: str
    product_kind: str
    state: str
    product_group_types: list[ProductGroupTypes]


class Categories(BaseModel):
    product_group: list[ProductGroup]



class InventoryGroups(BaseModel):
    group_code: str | None
    type_code: str | None


class InventoryKinds(BaseModel):
    inventory_kind: str | None


class InventorySectorCodes(BaseModel):
    sector_code: str | None


class InventoryItem(BaseModel):
    code: str | None
    name: str | None
    short_name: str | None
    weight_netto: str | None
    weight_brutto: str | None
    litr: str | None
    box_type_code: str | None
    box_quant: str | None
    producer_code: str | None
    measure_code: str | None
    state: str | None
    order_no: str | None
    article_code: str | None
    barcodes: str | None
    groups: list[InventoryGroups] | None
    inventory_kinds: list[InventoryKinds] | None
    sector_codes: list[InventorySectorCodes] | None


class Inventory(BaseModel):
    inventory: list[InventoryItem]
