import json
from Event import Event


class EventsJSON:
    def __init__(self, file_name):
        self.file_name = file_name
        self.__json_obj = json.dumps({})

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        if not isinstance(value, str):
            raise TypeError('File name must be a string!')
        self.__file_name = value

    def add_obj(self, obj):
        if not isinstance(obj, Event):
            raise TypeError('Object must be Event type!')
        json_dict = json.loads(self.__json_obj)
        json_dict[getattr(obj, 'id')] = obj.get_dict()
        self.__json_obj = json.dumps(json_dict)
        with open(self.file_name + '.json', 'w') as file:
            json.dump(json_dict, file, indent=4)

    def del_obj(self, obj):
        if not isinstance(obj, Event):
            raise TypeError('Object must be Event type!')
        json_dict = json.loads(self.__json_obj)
        del json_dict[str(getattr(obj, 'id'))]
        self.__json_obj = json.dumps(json_dict)
        with open(self.file_name + '.json', 'w') as file:
            json.dump(json_dict, file, indent=4)
