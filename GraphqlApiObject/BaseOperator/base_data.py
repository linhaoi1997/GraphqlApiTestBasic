import copy


class BaseData:

    def __init__(self, data_template=None):
        if data_template:
            self.__dict__ = copy.copy(data_template.__dict__)
        self.setup()

    def setup(self):
        pass
