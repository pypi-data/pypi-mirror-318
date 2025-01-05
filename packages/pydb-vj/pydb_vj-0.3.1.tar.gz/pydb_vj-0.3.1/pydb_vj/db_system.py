import json
import os

class DataBase:
    def __init__(self, source_path: str) -> None:
        current_dir = os.path.dirname(__file__)
        self.source_path = source_path


    def read(self, name: str) -> dict:
        full_path = f"{self.source_path}/{name}"

        with open(full_path, 'r') as file:
            data = json.load(file)

        return data
    
    def save(self, name: str, new_data: any) -> None:
        full_path = f"{self.source_path}/{name}"
        
        with open(full_path, "w") as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)

    def add_element(self, name: str, key: any, data: dict):
        old_data = self.read(name=name)
        old_data[key] = data

        self.save(name=name, new_data=old_data)

    def edit_element(self, name: str, key: any, low_data: dict):
        data = self.read(name=name)
        current_data: dict = data[key]

        for key_el in list(current_data.keys()):
            if low_data.get(key_el) is not None:
                current_data[key_el] = low_data[key_el]

        self.add_element(name=name, key=key, data=current_data)




