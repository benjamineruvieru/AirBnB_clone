#!/usr/bin/python3
"""File system engin module"""
from json import JSONDecoder, JSONEncoder


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
        return
