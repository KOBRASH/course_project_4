from api import HeadHunterAPI, SuperJobAPI
from json_saver import JSONSaver

class UserInterface:
    def __init__(self):
        """
        Инициализация объекта UserInterface.

        Устанавливает доступные провайдеры API и объект JSONSaver для работы с вакансиями.
        """
        self.api_providers = {
            "hh.ru": HeadHunterAPI("https://api.hh.ru/"),
            "superjob.ru": SuperJobAPI("https://api.superjob.ru/", api_key=""),
        }
        self.json_saver = JSONSaver("data/vacancies.json")
        self.json_saver.load_from_json()

    def get_vacancies_from_providers(self, search_query):
        """
        Получение списка вакансий с разных провайдеров.

        Args:
            search_query (str): Поисковый запрос.

        Returns:
            list: Список объектов Vacancy с вакансиями.
        """
        vacancies = []
        for provider_name, api in self.api_providers.items():
            provider_vacancies = api.get_vacancies(search_query)
            vacancies.extend(provider_vacancies)
        return vacancies

    def run(self):
        """
        Запуск пользовательского интерфейса.

        Пользователь вводит поисковый запрос, получает вакансии с провайдеров, и может сохранить их в файл.
        """
        search_query = input("Введите поисковый запрос: ")
        vacancies = self.get_vacancies_from_providers(search_query)

        if not vacancies:
            print("Нет доступных вакансий.")
            return

        print("Доступные вакансии:")
        for i, vacancy in enumerate(vacancies, start=1):
            print(f"{i}. {vacancy}")

        choice = input("Выберите действие (1 - Сохранить вакансии в файл, 2 - Выход): ")
        if choice == "1":
            for vacancy in vacancies:
                self.json_saver.add_vacancy(vacancy)
            self.json_saver.save_to_json()
            print("Вакансии сохранены в файле.")
        else:
            print("Выход из программы.")
