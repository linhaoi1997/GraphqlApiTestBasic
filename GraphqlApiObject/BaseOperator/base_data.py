class BaseData:

    def __init__(self, data_template=None):
        if data_template:
            self.__dict__ = data_template.__dict__
