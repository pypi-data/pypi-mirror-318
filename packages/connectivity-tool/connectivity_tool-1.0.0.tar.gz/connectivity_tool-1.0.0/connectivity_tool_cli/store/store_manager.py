from threading import Lock

from connectivity_tool_cli.store.jsonl_store import JsonlStore
from connectivity_tool_cli.store.store_base import StoreBase


class StoreManager:
    _instance: StoreBase = None
    _lock = Lock()

    def __init__(self, path: str):
        if StoreManager._instance is not None:
            raise RuntimeError("StoreManager is already initialized. Use `JsonlStoreManager.get_instance()`.")
        StoreManager._instance = JsonlStore(path)

    @classmethod
    def initialize(cls, path: str):
        with cls._lock:
            if cls._instance is None:
                cls(path)

    @classmethod
    def store(cls) -> StoreBase:
        if cls._instance is None:
            raise RuntimeError("StoreManager is not initialized. Call `initialize(path)` first.")
        return cls._instance
