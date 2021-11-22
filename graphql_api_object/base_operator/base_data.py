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

    def create_all_resource(self):
        for i in dir(self):
            logging.info(getattr(self, i))
