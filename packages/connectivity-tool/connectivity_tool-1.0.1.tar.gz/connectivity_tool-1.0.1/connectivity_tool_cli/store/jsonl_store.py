from connectivity_tool_cli.models.conn_result import ConnResult
from connectivity_tool_cli.store.jsonl_handler import JsonLineHandler
from connectivity_tool_cli.store.store_base import StoreBase


class JsonlStore(StoreBase):
    def __init__(self, path: str):
        self.jsonl_handler = JsonLineHandler(path)

    def log_results(self, result: ConnResult):
        self.jsonl_handler.append(result.to_dics())

    def get_last_result(self, curr_result: ConnResult) -> ConnResult | None:
        for result in self.jsonl_handler.iterate(reverse=True):
            if result['protocol'] == curr_result.protocol\
                    and result['asset'] == curr_result.asset:
                return ConnResult.from_dict(result)
        return None