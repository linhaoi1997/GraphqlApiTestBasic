import copy
import logging


class BaseData:

    def __init__(self, data_template=None):
        if data_template:
            self.__dict__ = copy.copy(data_template.__dict__)
        else:
            self.setup()

    def setup(self):
        pass

    def create_all_resource(self, exclude=None):
        if exclude is None:
            exclude = []
        for i in dir(self):
            if i not in exclude:
                logging.info(getattr(self, i))
