from abc import ABC, abstractmethod
from typing import Dict, Any

class MediaFile(ABC):
    """Базовый класс для медиа-файлов."""

    def __init__(self, file_path: str, metadata: Dict[str, Any], owner: str):
        self.file_path = file_path
        self.metadata = metadata
        self.owner = owner

    @abstractmethod
    def load_metadata(self) -> None:
        """Загрузить мета-данные файла."""
        pass

    @abstractmethod
    def save(self) -> None:
        """Сохранить файл."""
        pass

    @abstractmethod
    def update(self, updated_metadata: Dict[str, Any]) -> None:
        """Обновить метаданные файла."""
        pass

    @abstractmethod
    def delete(self) -> None:
        """Удалить файл."""
        pass

    @abstractmethod
    def extract_features(self) -> dict:
        """Извлечь особые характеристики файла."""
        pass


class AudioFile(MediaFile):
    """Класс для работы с аудиофайлами."""

    def load_metadata(self):
        pass

    def save(self):
        pass

    def update(self, updated_metadata):
        pass

    def delete(self):
        pass

    def extract_features(self):
        pass


class VideoFile(MediaFile):
    """Класс для работы с видеофайлами."""

    def load_metadata(self):
        pass

    def save(self):
        pass

    def update(self, updated_metadata):
        pass

    def delete(self):
        pass

    def extract_features(self):
        pass


class ImageFile(MediaFile):
    """Класс для работы с изображениями."""

    def load_metadata(self):
        pass

    def save(self):
        pass

    def update(self, updated_metadata):
        pass

    def delete(self):
        pass

    def extract_features(self):
        pass