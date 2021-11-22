from typing import List

from .base_operator import BaseOperator


class IdDictBuilder:

    @staticmethod
    def id(operator: BaseOperator):
        return operator.id

    @staticmethod
    def id_to_list(operator: BaseOperator):
        return [operator.id]

    @staticmethod
    def id_to_dict_list(operator: BaseOperator):
        return [{"id": operator.id}]

    @staticmethod
    def id_dict(operator: BaseOperator):
        return {"id": operator.id}

    @staticmethod
    def id_list(operators: List[BaseOperator]):
        return [i.id for i in operators]

    @staticmethod
    def id_dict_list(operators: List[BaseOperator]):
        return [{"id": i.id} for i in operators]
