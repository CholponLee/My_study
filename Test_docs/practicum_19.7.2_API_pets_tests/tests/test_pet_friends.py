from pets.api import PetFriends
from pets.settings import valid_email, valid_password, not_valid_email, not_valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем, что запрос api ключа возвращает статус 200 и
        в результате содержится слово key, также проверяем конкретное значение api ключа"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
    assert result['key'] == '119501f6c7c86a7d18ac75d315ca8c636611d6fe1ff500b09b4b2daf'


def test_get_api_key_for_not_valid_email(email=not_valid_email, password=valid_password):
    """ Проверяем, что запрос api ключа с неверным email пользователя
        возвращает статус 403 и в результате не содержится слово key"""
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_get_api_key_for_not_valid_password(email=valid_email, password=not_valid_password):
    """ Проверяем, что запрос api ключа с неверным паролем пользователя
        возвращает статус 403 и в результате не содержится слово key"""
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert 'key' not in result


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем, что запрос списка всех питомцев возвращает не пустой список"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Kate', animal_type='Кошка', age='1', pet_photo='images/cat3.jpg'):
    """ Проверяем, что запрос на добавление нового питомца
         с указанными корректными параметрами выполняется успешно"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_with_negative_age(name='Gera', animal_type='Собака', age='-1', pet_photo='images/dog1.jpg'):
    """ Проверяем, что запрос на добавление нового питомца
         с отрицательным возрастом выполняется успешно"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_with_empty_name(name='', animal_type='Кошка', age='2', pet_photo='images/cat3.jpg'):
    """ Проверяем, что запрос на добавление нового питомца
         с пустым полем имени выполняется успешно"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo(name='Kate', animal_type='Кошка', age='2'):
    """Проверяем, что возможность добавления питомца без фото
    выполняется успешно"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_successful_delete_self_pet():
    """Проверяем, что возможность удаления питомца
    выполняется успешно"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Суперкошка', 'Кошка', '3', 'images/cat1.jpg')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    pet_id = my_pets['pets'][1]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_pet_info(name='Ника', animal_type='Собака', age='7'):
    """Проверяем, что возможность обновления данных питомца
    выполняется успешно"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("Список моих питомцев пустой")
