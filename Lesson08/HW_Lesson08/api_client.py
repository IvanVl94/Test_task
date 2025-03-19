import requests

class Yougile:


    def __init__(self, base_url, token ):
        self.base_url = base_url
        self.headers = {
            "Authorization": "Bearer yOInDOF8DUYaY3sET7mPVdigX9oOwuLYNpYD3i2ftx4C5Mhoil-s09F9oKRCz4iY",
            "Content-Type": "application/json"
            }
        

    def create_project(self, project_data):
        response = requests.post(f"{self.base_url}/api-v2/projects", headers=self.headers, json=project_data)
        return response

    def update_project(self, project_id, project_data):
        response = requests.put(f"{self.base_url}/api-v2/projects/{project_id}", headers=self.headers, json=project_data)
        return response

    def get_project(self, project_id):
        response = requests.get(f"{self.base_url}/api-v2/projects/{project_id}", headers=self.headers)
        return response
