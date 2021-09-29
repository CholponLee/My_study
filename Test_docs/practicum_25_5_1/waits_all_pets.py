import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(r'E:\Skillfactory\Модуль 25\chromedriver.exe')

    # Неявное ожидание
    pytest.driver.implicitly_wait(10)
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    # Явное ожидание видимости поля для ввода email на экране
    WebDriverWait(pytest.driver, 5).until(
        EC.visibility_of_element_located((By.ID, 'email'))
    )
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('cholpon_lee@mail.ru')


    # Явное ожидание видимости поля для ввода пароля на экране
    WebDriverWait(pytest.driver, 5).until(
        EC.visibility_of_element_located((By.ID, 'pass'))
    )
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('700301')


    # Явное ожидание активности кнопки входа на сайт ("Войти")
    WebDriverWait(pytest.driver, 7).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    # Проверяем, что вошли в аккаунт
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


    # Записываем все фото, имена и описание питомцев в переменные
    # Неявное ожидание
    pytest.driver.implicitly_wait(7)
    images = pytest.driver.find_elements(By.CLASS_NAME, 'card-img-top')
    # Неявное ожидание
    pytest.driver.implicitly_wait(7)
    names = pytest.driver.find_elements(By.CLASS_NAME, 'card-title')
    # Неявное ожидание
    pytest.driver.implicitly_wait(7)
    descriptions = pytest.driver.find_elements(By.CLASS_NAME, 'card-text')

    # Проверяем, что имен питомцев больше нуля, то есть, что количествов питомцев больше нуля
    assert len(names) > 0

    # Проверяем наличие фото, имени и описания питомца
    for i in range(len(names)):
        try:
            assert images[i].get_attribute('src') != ''
        except AssertionError:
            print(f'Питомец {i+1} без фото')
        
        try:
            assert names[i].text != ''
        except AssertionError:
            print(f'Питомец {i+1} без имени')

        try:
            assert descriptions[i].text != ''
        except AssertionError:
            print(f'Питомец {i+1} без описания')


        parts = descriptions[i].text.split(',')
        try:
            assert len(parts[0]) > 0
        except AssertionError:
            print(f'У питомца {i+1} не указана порода')


        age = parts[1].split(' ')
        try:
            assert len(age[1]) > 0
        except AssertionError:
            print(f'У питомца {i+1} не указан возраст')

        try:
            age[1] == float(age[1])
        except ValueError:
            print(f'У питомца {i+1} некорректно указан возраст')
