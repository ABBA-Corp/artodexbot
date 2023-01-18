from sqlalchemy import Column, BigInteger, String, Integer

from tgbot.db.models import Base


class Order(Base):

    __tablename__ = 'order'

    user_id = Column(BigInteger, nullable=False, autoincrement=False, primary_key=True)
    name = Column(String(length=60), nullable=False)
    product_code = Column(String(length=60), nullable=False)
    count = Column(Integer, nullable=False)

    def __str__(self):
        return f'{self.user_id=}\n' \
               f'{self.name=}\n' \
               f'{self.product_code=}\n' \
               f'{self.count=}\n'
