import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                        'Authorization': f'OAuth {token}'}

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        file_name = file_path.split("\\")[-1]
        res = requests.get(f'{self.url}/upload?path={file_name}&overwrite=True', headers=self.headers).json()
        with open(file_path, 'rb') as f:
            try:
                requests.put(res['href'], files={'file': f})
            except KeyError:
                return res


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ""
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
