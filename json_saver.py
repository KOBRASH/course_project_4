import json
from vacancy import Vacancy

class JSONSaver:
    def __init__(self, filename):
        """
        Инициализация объекта JSONSaver.

        Args:
            filename (str): Имя файла для сохранения данных.
        """
        self.filename = filename
        self.vacancies = []

        # Проверяем наличие файла и создаем его при отсутствии
        try:
            with open(self.filename, "r", encoding="utf-8"):
                pass
        except FileNotFoundError:
            with open(self.filename, "w", encoding="utf-8"):
                pass

    def add_vacancy(self, vacancy):
        """
        Добавление вакансии в список.

        Args:
            vacancy (Vacancy): Объект вакансии для добавления.
        """
        self.vacancies.append(vacancy)

    def get_vacancies_by_salary(self, min_salary, max_salary):
        """
        Получение вакансий, удовлетворяющих заданным критериям зарплаты.

        Args:
            min_salary (str): Минимальная зарплата.
            max_salary (str): Максимальная зарплата.

        Returns:
            list: Список объектов Vacancy, удовлетворяющих критериям зарплаты.
        """
        filtered_vacancies = []
        for vacancy in self.vacancies:
            if vacancy.salary:
                salary = vacancy.salary.lower().replace(" ", "")

                if "—" in salary:
                    salary_range = salary.split("—")
                    min_salary_value = int(salary_range[0])
                    max_salary_value = int(salary_range[1].replace("руб.", ""))

                    if min_salary_value >= min_salary and max_salary_value <= max_salary:
                        filtered_vacancies.append(vacancy)

                elif "от" in salary:
                    min_salary_value = int(salary.replace("от", "").replace("руб.", ""))

                    if min_salary_value >= min_salary:
                        filtered_vacancies.append(vacancy)

                elif "до" in salary:
                    max_salary_value = int(salary.replace("до", "").replace("руб.", ""))

                    if max_salary_value <= max_salary:
                        filtered_vacancies.append(vacancy)

        return filtered_vacancies

    def delete_vacancy(self, vacancy):
        """
        Удаление вакансии из списка.

        Args:
            vacancy (Vacancy): Объект вакансии для удаления.
        """
        self.vacancies.remove(vacancy)

    def save_to_json(self):
        """Сохранение списка вакансий в JSON-файл."""
        with open(self.filename, "w") as file:
            json.dump([vars(vacancy) for vacancy in self.vacancies], file)

    def load_from_json(self):
        """Загрузка списка вакансий из JSON-файла, если файл существует."""
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.vacancies = [Vacancy(**item) for item in data]
        except FileNotFoundError:
            pass
