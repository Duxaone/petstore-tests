import requests
import pytest
import random
import time

BASE_URL = "https://petstore.swagger.io/v2"
PET_ID = random.randint(1000000, 9999999)


@pytest.mark.order(1)
def test_create_pet():
    """Создание питомца"""
    url = f"{BASE_URL}/pet"
    payload = {
        "id": PET_ID,
        "name": "Barsik",
        "status": "available"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Ошибка при создании питомца: {response.text}"
    assert response.json()["id"] == PET_ID
    time.sleep(1)  # даём время серверу обновиться


@pytest.mark.order(2)
def test_get_pet():
    """Получение питомца по ID"""
    url = f"{BASE_URL}/pet/{PET_ID}"
    response = requests.get(url)
    assert response.status_code == 200, f"Питомец не найден: {response.text}"
    data = response.json()
    assert data["name"] == "Barsik"
    assert data["status"] == "available"


@pytest.mark.order(3)
def test_update_pet():
    """Обновление данных питомца"""
    url = f"{BASE_URL}/pet"
    payload = {
        "id": PET_ID,
        "name": "BarsikUpdated",
        "status": "sold"
    }
    response = requests.put(url, json=payload)
    assert response.status_code == 200, f"Ошибка при обновлении: {response.text}"

    # Проверяем, что обновления применились
    response = requests.get(f"{BASE_URL}/pet/{PET_ID}")
    assert response.json()["status"] == "sold"


@pytest.mark.order(4)
def test_delete_pet():
    """Удаление питомца"""
    url = f"{BASE_URL}/pet/{PET_ID}"
    response = requests.delete(url)
    assert response.status_code == 200, f"Ошибка при удалении питомца: {response.text}"

    # Проверяем, что питомец действительно удален
    for _ in range(3):
        time.sleep(1)
        check = requests.get(url)
        if check.status_code == 404:
            break
    assert check.status_code == 404, "Питомец не был удален"
