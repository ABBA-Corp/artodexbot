from sqlalchemy import Column, BigInteger, String, Integer

from tgbot.db.models import Base


class Order(Base):

    __tablename__ = 'order'

    id = Column(BigInteger, nullable=False, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, nullable=False, autoincrement=False, primary_key=False)
    name = Column(String(length=60), nullable=False)
    product_code = Column(String(length=60), nullable=False)

    def __str__(self):
        return f'{self.id}' \
               f'{self.user_id=}\n' \
               f'{self.name=}\n' \
               f'{self.product_code=}\n'
