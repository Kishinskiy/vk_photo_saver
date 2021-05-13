import os
import time
import tqdm

from dotenv import load_dotenv  # for python-dotenv method
from VkDownloader import VK
from YaDiskUploader import YaUploader

load_dotenv()

vk_access_token = os.environ.get('vk_access_token')
vk_api_version = os.environ.get('vk_api_version')
yandex_disk_token = os.environ.get('yandex_disk_token')
vk = VK(vk_access_token, vk_api_version)
uploader = YaUploader(yandex_disk_token)
folder = 'vk_photos'


def get_url_photo(count):
    photo_url = []
    for photo in vk.get_photos(count)['response']['items']:
        size = photo['sizes'][-1:][0]['url']
        photo_url.append(size)
    return photo_url


def upload_to_yadisk(file_name, file_url):
    time.sleep(1)
    return uploader.upload_from_url(file_name, file_url)


def main():
    n = 0
    print(uploader.create_folder(folder))
    for photo_url in tqdm.tqdm(get_url_photo(count=60)).bar_format:
        upload_to_yadisk(f'{folder}/vk_photo_{n}.png', photo_url) # индекс в имени файла нужен, так как без него сохранаяются только 4 файла вместо 5
        n += 1


if __name__ == '__main__':
    main()
    # print(vk.get_photos())