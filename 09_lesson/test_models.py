import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student  # Импортируем модель и базу

# Строка подключения к базе данных
DATABASE_URL = "postgresql://postgres:@localhost:5432/mydatabase"

# Создаем engine для подключения к базе данных
engine = create_engine(DATABASE_URL, echo=True)

# Создаем сессию
Session = sessionmaker(bind=engine)

@pytest.fixture(scope="function")
def session():
    """Тестовая сессия для каждого теста"""
    # Создаем таблицы (если они не существуют)
    Base.metadata.create_all(engine)

    # Создаем сессию
    session = Session()

    yield session  # Возвращаем сессию для использования в тестах

    # Удаляем данные после теста
    session.close()
    Base.metadata.drop_all(engine)

def test_add_student(session):
    """Тест для добавления студента"""
    student = Student(name="John Doe", age=22)
    session.add(student)
    session.commit()

    # Проверяем, что студент добавлен в базу данных
    result = session.query(Student).filter_by(name="John Doe").first()
    assert result is not None
    assert result.name == "John Doe"
    assert result.age == 22

def test_update_student(session):
    """Тест для изменения данных студента"""
    student = Student(name="Jane Doe", age=21)
    session.add(student)
    session.commit()

    # Обновляем данные студента
    student.age = 22
    session.commit()

    # Проверяем, что данные обновлены
    updated_student = session.query(Student).filter_by(name="Jane Doe").first()
    assert updated_student.age == 22

def test_delete_student(session):
    """Тест для удаления студента"""
    student = Student(name="Mike Ross", age=23)
    session.add(student)
    session.commit()

    # Удаляем студента
    session.delete(student)
    session.commit()

    # Проверяем, что студента больше нет в базе данных
    deleted_student = session.query(Student).filter_by(name="Mike Ross").first()
    assert deleted_student is None

