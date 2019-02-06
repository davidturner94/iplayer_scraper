import json


class DictionaryBuilder(object):
    """docstring for DictionaryBuilder"""

    def __init__(self):
        super(DictionaryBuilder, self).__init__()

        self.parent_dict = {}

    def print(self):
        print(self.parent_dict)

    def to_json(self):
        pass

    def update(self, key, value):
        try:
            self.parent_dict[key].update(value)
        except:
            print('key not valid')

    def add(self, value):
        self.parent_dict.update(value)

    def remove():
        pass
