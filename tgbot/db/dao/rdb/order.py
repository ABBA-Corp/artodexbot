from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.dao.rdb import BaseDAO
from tgbot.db.models import Order


class OrderDAO(BaseDAO[Order]):
    def __init__(self, session: AsyncSession):
        super().__init__(Order, session)

    async def add_order(
            self,
            user_id: int,
            name: str,
            product_code: str
    ):
        await self.session.execute(
            insert(Order).values(
                user_id=user_id,
                name=name,
                product_code=product_code
            )
        )
        await self.session.commit()

    async def get_all_orders(self) -> list[Order]:
        result = await self.session.execute(
            select(Order)
        )
        return result.scalars().all()
