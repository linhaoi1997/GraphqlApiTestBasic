from typing import Type, Dict
from functools import partial

from ..GraphqlApi import GraphqlQueryListAPi


class BaseQueryOperator(object):
    query_api = Type[GraphqlQueryListAPi]
    base_filter: Dict = {}
    filter_has_company: bool = True
    limit = 20
    offset = 0

    def __init__(self, user, company_id=None):
        self.user = user
        self.company_id = company_id or self.user.info["company"]["id"]
        self.base_filter["company"] = {"id": company_id}
        self._query_api: GraphqlQueryListAPi = self.query_api(self.user)

    def search_row(self, query_path, query_field, query_value, filter_dict: Dict):
        filter_dict.update(self.base_filter)
        return self._query_api.query(offset=self.offset, limit=self.limit, filter=filter_dict).c(
            f"{query_path}[?{query_field} == '{query_value}'] | [0]"
        )

    def filter_by(self, key, value):
        self._query_api.set_filter(key=value, **self.base_filter)
        return self._query_api.query()

    @property
    def ids(self):
        return self._query_api.ids

    def __getattr__(self, item: str):
        if item.startswith("filter_by_"):
            key = item.split("_")[-1]
            return partial(self.filter_by, key)
        else:
            raise AssertionError(f"QueryOperator object has no attribute named {item}")
