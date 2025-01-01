from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def upload(self, source_path: str, destination_path: str) -> None:
        """Upload a file to the storage backend."""
        pass

    @abstractmethod
    def download(self, source_path: str, destination_path: str) -> None:
        """Download a file from the storage backend."""
        pass

