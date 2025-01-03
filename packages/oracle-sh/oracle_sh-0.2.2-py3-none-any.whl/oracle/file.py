import json
from pathlib import Path


class File:
    def __init__(self, path: Path | str = Path.home() / ".oracle") -> None:
        self.path = Path(path) if path else Path.home() / ".oracle"

    def read(self) -> dict:
        try:
            return json.loads(self.path.read_text())
        except FileNotFoundError:
            # set a default for now
            return {"name": "oracle", "choices": []}

    def write(self, data: dict) -> None:
        self.path.write_text(json.dumps(data))
