from vacancy import Vacancy

def test_vacancy():
    title = "Python Developer"
    link = "https://example.com/job/123"
    salary = "100,000 - 150,000 руб."
    description = "Требования: опыт работы от 3 лет..."

    vacancy = Vacancy(title, link, salary, description)

    assert vacancy.title == title
    assert vacancy.link == link
    assert vacancy.salary == salary
    assert vacancy.description == description

def test_vacancy_str_representation():
    title = "Python Developer"
    link = "https://example.com/job/123"
    salary = "100,000 - 150,000 руб."
    description = "Требования: опыт работы от 3 лет..."

    vacancy = Vacancy(title, link, salary, description)

    expected_str = f"{title} ({salary}): {link}"
    assert str(vacancy) == expected_str
