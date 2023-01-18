from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.dao.rdb import BaseDAO
from tgbot.db.models import User


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def add_user(
            self,
            user_id: int,
            name: str,
            username: str | None,
            language: str,
            phone_number: str
    ):
        await self.session.execute(
            insert(User).values(
                user_id=user_id,
                name=name,
                username=username,
                language=language,
                phone_number=phone_number
            )
        )
        await self.session.commit()

    async def get_user(self, user_id: int) -> User:
        result = await self.session.execute(
            select(User).filter(
                User.user_id == user_id
            )
        )
        return result.scalar()

    async def get_all_users(self) -> list[User]:
        result = await self.session.execute(
            select(User)
        )
        return result.scalars().all()

    async def update_language(self, user_id: int, language: str):
        await self.session.execute(
            update(User).filter(
                User.user_id == user_id
            ).values(
                language=language
            )
        )
        await self.session.commit()

    async def edit_user_name(self, user_id: int, name: str):
        await self.session.execute(
            update(User).filter(
                User.user_id == user_id
            ).values(
                name=name
            )
        )
        await self.session.commit()

    async def edit_user_phone(self, user_id: int, phone: str):
        await self.session.execute(
            update(User).filter(
                User.user_id == user_id
            ).values(
                phone=phone
            )
        )
        await self.session.commit()
    