from api import HeadHunterAPI, SuperJobAPI

def test_headhunter_api():
    api = HeadHunterAPI("https://api.hh.ru/")
    vacancies = api.get_vacancies("Python")
    assert len(vacancies) > 0

def test_superjob_api():
    api = SuperJobAPI("https://api.superjob.ru/", api_key="your_api_key_here")
    vacancies = api.get_vacancies("Python")
    assert len(vacancies) > 0
