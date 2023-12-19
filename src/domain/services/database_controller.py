class DatabaseController:
    def execute(self, query: str, params: list[str]) -> list(str):
        raise NotImplementedError()