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


    # МОИ ИТОМЦЫ
    # Явное ожидание активности ссылки "Мои питомцы"
    WebDriverWait(pytest.driver, 7).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Мои питомцы'))
    )
    # Переходим на страницу Мои питомцы
    pytest.driver.find_element_by_link_text('Мои питомцы').click()
    # Проверяем, что попали на страницу Моих питомцев
    assert pytest.driver.find_element_by_tag_name('h2').text == 'Cholpon'

    # Записываем все фото, имена и описание Моих питомцев в переменные
    my_pets_names = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > '
                                                                 'td:nth-of-type(1)')
    my_pets_images = pytest.driver.find_elements(By.TAG_NAME, 'img')
    my_pets_breed = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > '
                                                                 'td:nth-of-type(2)')
    my_pets_age = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > '
                                                               'td:nth-of-type(3)')

    # Проверяем, что имен Моих питомцев больше нуля, то есть, что количествов Моих питомцев больше нуля
    assert len(my_pets_names) > 0

    # Проверяем карточки Моих питомцев на наличие фото, имени и описания
    for i in range(len(my_pets_names)):
        assert my_pets_images[i].get_attribute('src') != ''
        assert my_pets_names[i].text != ''
        assert my_pets_breed[i].text != ''
        assert my_pets_age[i].text != ''

    # Проверяем. что количетвов Моих питомцев соответствует количеству, указанному на сайте
    assert len(my_pets_names) == 95
