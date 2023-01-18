from sqlalchemy import Column, BigInteger, String

from tgbot.db.models import Base


class User(Base):

    __tablename__ = 'user'

    user_id = Column(BigInteger, nullable=False, autoincrement=False, primary_key=True)
    name = Column(String(length=60), nullable=False)
    username = Column(String(length=100), nullable=True)
    language = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

    def __str__(self):
        return f'{self.user_id=}\n' \
               f'{self.name=}\n' \
               f'{self.username=}\n' \
               f'{self.language=}\n' \
               f'{self.phone_number=}'
