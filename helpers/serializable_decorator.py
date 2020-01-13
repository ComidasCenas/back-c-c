import json


def serializable(Cls):
    class NewSerializableClass(Cls):
        def to_json(self):
            return json.dumps(self.__dict__, indent=4, sort_keys=True)

    return NewSerializableClass
