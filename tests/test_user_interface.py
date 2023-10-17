# test_user_interface.py
from user_interface import UserInterface

def test_user_interface():
    user_interface = UserInterface()

    # Тест ввода поискового запроса и получения вакансий
    user_interface.get_vacancies_from_providers("Python Developer")

    # Тест сохранения вакансий в файл
    user_interface.run()
