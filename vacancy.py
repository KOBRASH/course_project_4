# modules/vacancy.py

class Vacancy:
    def __init__(self, title, link, salary, description):
        """
        Инициализация объекта Vacancy.

        Args:
            title (str): Название вакансии.
            link (str): Ссылка на вакансию.
            salary (str): Зарплата.
            description (str): Описание вакансии.
        """
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __str__(self):
        """
        Возвращает строковое представление вакансии.

        Returns:
            str: Строковое представление вакансии.
        """
        return f"{self.title} ({self.salary}): {self.link}"
