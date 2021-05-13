import requests


class YaUploader:
    def __init__(self, token: str):
        self.url_requests = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.token = token
        self.headers = {"Authorization": f"OAuth {self.token}"}

    def get_upload_url(self, name: str):
        resp = requests.get(self.url_requests, headers=self.headers, params={
            'path': f'/{name}',
            'overwrite': 'true'
        })
        resp.raise_for_status()
        return resp.json()['href']

    def create_folder(self, folder_name):
        try:
            resp = requests.put(self.url_requests, headers=self.headers, params={
                'path': f'/{folder_name}'
            })
            resp.raise_for_status()
        except Exception as e:
            print(e)
            return 0
        return resp

    def upload_from_url(self, name, file_url):
        url_requests = f'{self.url_requests}/upload'
        resp = requests.post(url_requests, headers=self.headers, params={
            'url': file_url,
            'path': f'/{name}'
        })
        resp.raise_for_status()
        return resp
