import pytest
import requests
from api_client import Yougile

base_url = "https://ru.yougile.com/api-v2/"


@pytest.fixture
def yougile_api():
    base_url = "https://ru.yougile.com"
    token = "Bearer yOInDOF8DUYaY3sET7mPVdigX9oOwuLYNpYD3i2ftx4C5Mhoil-s09F9oKRCz4iY"

    return Yougile(base_url, token)


# Добавить проект (позитивная проверка)

def test_create_project_positive(yougile_api):
    project_data = {"title": "Python-8.3"}
    response = yougile_api.create_project(project_data)
    assert response.status_code == 201, f"Response Body:{response.text}"


# Добавить проект (позитивная проверка)
def test_create_project_negative(yougile_api):
    project_data = {}
    response = yougile_api.create_project(project_data)
    assert response.status_code == 400


# Изменить Id проекта

def test_update_project_positive(yougile_api):
    project_data = {"title": "Python-8.3"}
    response = yougile_api.create_project(project_data)
    project_id = response.json()["id"]

    project_data_2 = {"title": "Python-8.4"}
    response = yougile_api.update_project(project_id, project_data_2)
    assert response.status_code == 200, f"Response Body:{response.text}"


def test_update_project_negative(yougile_api):
    project_id = 99999
    project_id = {
        "deleted": True,
        "title": "Python-8.3",
        "users": {
            "df9bcca1-2bdf-4722-b105-f09631290479": "admin"}
    }

    response = yougile_api.update_project(project_id, project_id)
    assert response.status_code == 404


# Изменить получить по  Id

def test_get_project_positive(yougile_api):
    project_data = {"title": "Python-8.3"}
    response = yougile_api.create_project(project_data)
    project_id = response.json()["id"]

    response = yougile_api.get_project(project_id)
    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative(yougile_api):
    project_id = 99999

    response = yougile_api.get_project(project_id)
    assert response.status_code == 404


