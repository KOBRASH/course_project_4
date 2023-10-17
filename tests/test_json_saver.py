from json_saver import JSONSaver
from vacancy import Vacancy

def test_json_saver_add_and_delete_vacancy():
    filename = "test.json"
    json_saver = JSONSaver(filename)
    vacancy = Vacancy("Python Developer", "https://example.com/job/123", "100,000 - 150,000 руб.", "Требования: опыт работы от 3 лет...")

    json_saver.add_vacancy(vacancy)
    assert vacancy in json_saver.vacancies

    json_saver.delete_vacancy(vacancy)
    assert vacancy not in json_saver.vacancies

def test_json_saver_get_vacancies_by_salary():
    filename = "test.json"
    json_saver = JSONSaver(filename)
    vacancy1 = Vacancy("Python Developer", "https://example.com/job/123", "100,000 - 150,000 руб.", "Требования: опыт работы от 3 лет...")
    vacancy2 = Vacancy("Java Developer", "https://example.com/job/456", "80,000 - 120,000 руб.", "Требования: опыт работы от 2 лет...")

    json_saver.add_vacancy(vacancy1)
    json_saver.add_vacancy(vacancy2)

    filtered_vacancies = json_saver.get_vacancies_by_salary(90_000, 140_000)
    assert vacancy1 in filtered_vacancies
    assert vacancy2 not in filtered_vacancies
