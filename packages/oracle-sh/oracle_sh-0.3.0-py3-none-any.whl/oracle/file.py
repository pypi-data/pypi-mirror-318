import json
from pathlib import Path

from oracle.model.group import ChoiceGroup


class File:
    def __init__(self, path: Path | str = Path.home() / ".oracle") -> None:
        self.path = Path(path) if path else Path.home() / ".oracle"

    def read(self) -> ChoiceGroup:
        try:
            data = json.loads(self.path.read_text())
            return ChoiceGroup(**data)
        except FileNotFoundError:
            group = ChoiceGroup()
            self.write(group)
            return self.read()

    def write(self, data: ChoiceGroup = ChoiceGroup()) -> None:
        self.path.write_text(data.model_dump_json())
