import requests


class VK:
    def __init__(self, token, version):
        self.url = 'https://api.vk.com/method/'
        self.token = token
        self.version = version
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_user(self, id):
        url = self.url + 'users.get'
        user_params = {
            'user_id': id
        }
        return requests.get(url, params={**self.params, **user_params}).json()

    def get_photos(self, count=5):
        url = self.url + 'photos.get'
        photos_params = {
            'album_id': 'wall',
            'count': count
        }
        return requests.get(url, params={**self.params, **photos_params}).json()
