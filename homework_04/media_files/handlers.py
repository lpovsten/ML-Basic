from models import MediaFile

class LocalStorageHandler:
    """Хранилище на локальном диске."""

    def store_file(self, media_file: MediaFile):
        print(f"Сохранен файл {media_file.file_path} на локальном диске.")

    def retrieve_file(self, path: str) -> MediaFile:
        print(f"Загружен файл {path} с локального диска.")
        return None

    def remove_file(self, path: str):
        print(f"Удален файл {path} с локального диска.")


class CloudStorageHandler:
    """Хранилище в облаке."""

    def store_file(self, media_file: MediaFile):
        print(f"Сохранен файл {media_file.file_path} в облаке.")

    def retrieve_file(self, cloud_path: str) -> MediaFile:
        print(f"Загружен файл {cloud_path} из облака.")
        return None

    def remove_file(self, cloud_path: str):
        print(f"Удален файл {cloud_path} из облака.")


class RemoteServerStorageHandler:
    """Хранилище на удалённом сервере."""

    def store_file(self, media_file: MediaFile):
        print(f"Сохранен файл {media_file.file_path} на удалённом сервере.")

    def retrieve_file(self, remote_url: str) -> MediaFile:
        print(f"Загружен файл {remote_url} с удалённого сервера.")
        return None

    def remove_file(self, remote_url: str):
        print(f"Удален файл {remote_url} с удалённого сервера.")