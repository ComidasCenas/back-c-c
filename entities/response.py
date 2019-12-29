import json


class Response():
    def __init__(self, status, body):
        self.status = status
        self.body = body

    # def to_json(self):
    #     return json.dumps(self.__dict__, indent=4, sort_keys=True)

    def __repr__(self):
        return json.dumps(self.__dict__)
