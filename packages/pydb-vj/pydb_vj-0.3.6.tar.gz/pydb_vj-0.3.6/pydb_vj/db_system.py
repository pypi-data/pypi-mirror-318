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

    def add_element(self, key: any, with_check: bool=True):
        old_data = self.read()
        if old_data.get(key) is None:
            old_data[key] = self.default_data
            self.save(new_data=old_data)
            return 0
        
        else:
            if with_check == False:
                old_data[key] = self.default_data
                self.save(new_data=old_data)
                return 1
            
        
        return 1

    def edit_element(self, key: any, low_data: dict):
        data = self.read()
        current_data: dict = data[key]

        for key_el in list(current_data.keys()):
            if low_data.get(key_el) is not None:
                current_data[key_el] = low_data[key_el]

        data[key] = current_data
        self.save(data)

    def find_element(self, key) -> dict:
        data = self.read()
        return data.get(key)
    
    def update_data(self):
        old_data = self.read()
        update_data = []
        for global_key in old_data:
            for key in self.default_data:
                if old_data[global_key].get(key) is not None:
                    update_data[global_key][key] = old_data[global_key].get(key)
                else:
                    update_data[global_key][key] = self.default_data[key]

        self.save(update_data)






