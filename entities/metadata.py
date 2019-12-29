import json


class Metadata():
    def __init__(self, offset, limit, total, sort, direction):
        self.offset = offset
        self.limit = limit
        self.total = total
        self.sort = sort
        self.direction = direction

    def to_json(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True)
