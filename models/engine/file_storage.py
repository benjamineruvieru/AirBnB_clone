#!/usr/bin/python3
"""File system engin module"""
import os
from json import JSONDecoder, JSONEncoder
from importlib import import_module


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns dictionary representation"""
        return FileStorage.__objects

    @setter
    def new(self, obj):
        """sets __objects the obj with key"""
        dict_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[dict_key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, mode='w') as file:
            json_format = {}
            for key, value in FileStorage.__objects.items():
                json_format[key] = value.to_dict()
            file.write(JSONEncoder().encode(json_format))

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON file exists
        """
        """Deserializes the JSON file to objects if it exists.
        """
        if os.path.isfile(self.__file_path):
            file_lines = []
            with open(self.__file_path, mode='r') as file:
                file_lines = file.readlines()
            file_txt = ''.join(file_lines) if len(file_lines) > 0 else '{}'
            json_objs = JSONDecoder().decode(file_txt)
            base_model_objs = dict()
            classes = self.model_classes
            for key, value in json_objs.items():
                class_name = value['__class__']
                if class_name in classes.keys():
                    base_model_objs[key] = classes[class_name](**value)
            self.__objects = base_model_objs
