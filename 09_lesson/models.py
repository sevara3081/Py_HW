from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем базовый класс для моделей
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    # Определяем поля таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

# Подключение к базе данных PostgreSQL
DATABASE_URL = "postgresql://postgres:@localhost:5432/mydatabase"  # ваша строка подключения

# Создаем engine для подключения к базе данных
engine = create_engine(DATABASE_URL, echo=True)

# Сессия для работы с БД
Session = sessionmaker(bind=engine)

# Создаем таблицы в базе данных
Base.metadata.create_all(engine)