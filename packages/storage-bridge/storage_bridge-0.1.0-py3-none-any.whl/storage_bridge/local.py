import os

from starcraft_data_orm.storage.storage import Storage

class LocalStorage(Storage):
    def __init__(self, base_path: str = "./storage"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    def upload(self, source_path: str, destination_path: str) -> None:
        dest = os.path.join(self.base_path, destination_path)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        os.rename(source_path, dest)
        print(f"Uploaded to local storage: {dest}")

    def download(self, source_path: str, destination_path: str) -> None:
        src = os.path.join(self.base_path, source_path)
        os.rename(src, destination_path)
        print(f"Downloaded from local storage: {src}")
        return destination_path

    def list_files(self):
        return os.listdir(self.base_path)

