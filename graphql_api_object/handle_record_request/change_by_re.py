import re


def to_str(id_):
    def _to_str(matched):
        return "".join(matched.groups()[:-1]) + id_

    return _to_str


def change_by_re(msg: str, patterns: list[str], operators: list[{id}] or {id}) -> str:
    pattern = f"({'|'.join(patterns)}).*?id.*?(\d+)"
    all_need_changes = re.findall(pattern, msg)
    cache = {}
    index = 0
    for i in all_need_changes:
        name = i[0]
        id_ = i[1]
        if not cache.get(id_):
            cache[id_] = str(operators[index].id)
            index += 1
        msg = re.sub(f"({name})(.*?id.*?)({id_})", to_str(cache.get(id_)), msg)
    return msg
