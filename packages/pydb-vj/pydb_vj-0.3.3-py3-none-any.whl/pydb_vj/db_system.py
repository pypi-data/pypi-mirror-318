import json
import os

class DataBase:
    def __init__(self, name: str, source_path: str, default_data: dict, file_path: str) -> None:
        current_dir = os.path.dirname(file_path)
        self.source_path = f"{current_dir}/{source_path}"

        self.default_data = default_data
        self.name = name


    def read(self) -> dict:
        full_path = f"{self.source_path}/{self.name}"

        with open(full_path, 'r') as file:
            data = json.load(file)

        return data
    
    def save(self, new_data: any) -> None:
        full_path = f"{self.source_path}/{self.name}"
        
        with open(full_path, "w") as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)

    def add_element(self, key: any):
        old_data = self.read()

        if old_data.get(key) is None:
            old_data[key] = self.default_data
            self.save(name=self.name, new_data=old_data)
            return 0
        
        return -1

    def edit_element(self, key: any, low_data: dict):
        data = self.read(name=self.name)
        current_data: dict = data[key]

        for key_el in list(current_data.keys()):
            if low_data.get(key_el) is not None:
                current_data[key_el] = low_data[key_el]

        self.add_element(name=self.name, key=key, data=current_data)

    def find_element(self, key) -> dict:
        data = self.read(name=self.name)
        return data[key]





