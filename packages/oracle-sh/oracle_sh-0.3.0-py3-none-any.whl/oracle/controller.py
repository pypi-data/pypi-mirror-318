from oracle.display import Display
from oracle.file import File
from oracle.model.group import ChoiceGroup


class Controller:
    def __init__(self, file: File | None = None, display: Display | None = None) -> None:
        self.file = file if file else File()
        self.display = display if display else Display()
        self.group: ChoiceGroup = ChoiceGroup()
        self.refresh()

    def refresh(self) -> None:
        try:
            self.group = self.file.read()
        except FileNotFoundError:
            self.group = ChoiceGroup()

    def save(self) -> None:
        self.file.write(self.group)
