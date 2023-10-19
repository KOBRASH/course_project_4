import requests
from abc import ABC, abstractmethod
from vacancy import Vacancy

class VacancyAPI(ABC):
    def __init__(self, base_url, api_key=None):
        """
        Инициализация объекта VacancyAPI.

        Args:
            base_url (str): Базовый URL для API сайта.
            api_key (str, optional): API-ключ (по умолчанию None).
        """
        self.base_url = base_url
        self.api_key = api_key


    def get_vacancies(self, search_query):
        """
        Абстрактный метод для получения списка вакансий.

        Args:
            search_query (str): Поисковый запрос.

        Returns:
            list: Список объектов Vacancy, представляющих вакансии.
        """
        pass

    def parse_response(self, response):
        pass

class HeadHunterAPI(VacancyAPI):
    def get_vacancies(self, search_query):
        """
        Получение списка вакансий с сайта HeadHunter.

        Args:
            search_query (str): Поисковый запрос.

        Returns:
            list: Список объектов Vacancy, представляющих вакансии с HeadHunter.
        """
        url = f"{self.base_url}vacancies"
        params = {
            "text": search_query,
            "area": 1,  # Москва
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            vacancies = response.json().get("items", [])
            return [Vacancy(vacancy["name"], vacancy["alternate_url"], vacancy["salary"], vacancy["snippet"]["requirement"])
                    for vacancy in vacancies]
        else:
            print("Ошибка при запросе вакансий с HeadHunter:", response.status_code)
            return []
    def parse_response(self, response):
            vacancies = response.json().get("items", [])
            return [
                Vacancy(vacancy["name"], vacancy["alternate_url"], vacancy["salary"], vacancy["snippet"]["requirement"])
                for vacancy in vacancies]

class SuperJobAPI(VacancyAPI):
    def get_vacancies(self, search_query):
        """
        Получение списка вакансий с сайта SuperJob.

        Args:
            search_query (str): Поисковый запрос.

        Returns:
            list: Список объектов Vacancy, представляющих вакансии с SuperJob.
        """
        url = f"{self.base_url}vacancies/"
        headers = {
            "X-Api-App-Id": self.api_key,
        }
        params = {
            "count": 100,
            "keyword": search_query,
            "town": 4,
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            vacancies = response.json().get("objects", [])
            return [Vacancy(vacancy["profession"], vacancy["link"], vacancy["payment_from"], vacancy["candidat"])
                    for vacancy in vacancies]
        else:
            print("Ошибка при запросе вакансий с SuperJob:", response.status_code)
            return []
    def parse_response(self, response):
            vacancies = response.json().get("objects", [])
            return [Vacancy(vacancy["profession"], vacancy["link"], vacancy["payment_from"], vacancy["candidat"])
                    for vacancy in vacancies]