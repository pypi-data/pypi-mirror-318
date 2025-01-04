from rich.console import Console

console = Console()


class Display:
    def __init__(self, console: Console | None = None) -> None:
        self.console = console if console else Console()

    def show(self, message: str) -> None:
        self.console.print(message, overflow="ellipsis", no_wrap=True)

    # message types
    def indexed(self, index: int, message: str) -> None:
        self.show(f"[cyan bold][{index}][/] {message}")

    def success(self, message: str) -> None:
        self.show(f"[blue bold][*][/] {message}")

    def info(self, message: str) -> None:
        self.show(f"[green bold][+][/] {message}")

    def confused(self, message: str) -> None:
        self.show(f"[yellow bold][?][/] {message}")

    def warning(self, message: str) -> None:
        self.show(f"[red bold][!][/] {message}")

    def diagnostic(self, message: str) -> None:
        self.show(f"[white bold][?][/] {message}")
