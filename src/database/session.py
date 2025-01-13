from sqlalchemy.orm import sessionmaker
from src.core.db import engine


session = sessionmaker(bind=engine)


def get_db():
    print('Зашли в get_db')
    with session() as db:
        print('Отдаем подключение')
        yield db
        print('Убираем подключение')
    print('Выходим из get_db')
