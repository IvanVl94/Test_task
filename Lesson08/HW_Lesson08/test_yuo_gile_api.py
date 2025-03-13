
import pytest
import requests
from api_client import Yougile


base_url = "https://ru.yougile.com/api-v2/"

@pytest.fixture

def yougile_api():
    base_url = "https://ru.yougile.com/api-v2/" 
    token = "..."           
    return Yougile(base_url, token)

 

# Добавить проект (позитивная проверка)

def test_create_project_positive(yougile_api):
    project_data = {
        "title": "Python-8.3",
        "users": {
            "df9bcca1-2bdf-4722-b105-f09631290479": "admin"}
    }
    response = yougile_api.create_project(project_data)
    assert response.status_code == 201
    assert response.json().get("name") == project_data["name"]
    
# Добавить проект (позитивная проверка)
def test_create_project_negative(yougile_api):
    project_data = {}
    response = yougile_api.create_project(project_data)
    assert response.status_code == 401
    
    
# Изменить Id проекта

def test_update_project_positive(yougile_api):
    project_id = 1
    project_data = {
        "deleted": True,
        "title": "Python-8.3",
        "users": {
            "df9bcca1-2bdf-4722-b105-f09631290479": "admin"}
    }
    
    response = yougile_api.update_project(project_data, project_id)
    assert response.status_code == 200
    
def test_update_project_negative(yougile_api):
    project_id = 99999
    project_data = {
        "deleted": True,
        "title": "Python-8.3",
        "users": {
            "df9bcca1-2bdf-4722-b105-f09631290479": "admin"}
    }
    
    response = yougile_api.update_project(project_data, project_id)
    assert response.status_code == 401
    
# Изменить получить по  Id

def test_get_project_positive(yougile_api):
    project_id = 1
    
    response = yougile_api.get_project( project_id)
    assert response.status_code == 200
    assert response.json()("id") == project_id["id"]

def test_get_project_negative(yougile_api):
    project_id = 99999
    
    response = yougile_api.get_project(project_id)
    assert response.status_code == 401
    




























































def test_create_project_positive(yougile_api):
    project_data = {
        "name": "...",
        "description": "..."
    }
    response = yougile_api.create_project(project_data)
    assert response.status_code == 201
    assert response.json().get("name") == project_data["name"]

def test_create_project_negative(yougile_api):
    project_data = { }
    response = yougile_api.create_project(project_data)
    assert response.status_code == 400                     

def test_update_project_positive(yougile_api):
    project_id = 1                                          
    project_data = {
        "name": "",
        "description": ""
    }
    response = yougile_api.update_project(project_id, project_data)
    assert response.status_code == 200
    assert response.json().get("name") == project_data["name"]

# Не существующий ID
def test_update_project_negative(yougile_api):
    project_id = 9999                                              
    project_data = {
        "name": "New Project",
        "description": "This project won't be created."
    }
    response = yougile_api.update_project(project_id, project_data)
    assert response.status_code == 404                               

# Замените на существующий ID проекта
def test_get_project_positive(yougile_api):
    project_id = 1  
    response = yougile_api.get_project(project_id)
    assert response.status_code == 200
    assert response.json().get("id") == project_id

# Не существующий ID
def test_get_project_negative(yougile_api):
    project_id = 9999                                    # Не существующий ID
    response = yougile_api.get_project(project_id)
    assert response.status_code == 404