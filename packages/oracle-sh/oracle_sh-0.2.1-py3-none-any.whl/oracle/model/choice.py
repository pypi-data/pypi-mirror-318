from dataclasses import asdict, dataclass


@dataclass
class Choice:
    name: str
    trials: int = 0
    successes: int = 0

    def __hash__(self) -> int:
        return hash(self.id)

    def __str__(self) -> str:
        return self.name

    @property
    def json(self) -> dict:
        return asdict(self)

    def trial(self) -> None:
        self.trials += 1

    def success(self) -> None:
        self.trials += 1
        self.successes += 1

    def reset(self) -> None:
        self.trials = 0
        self.successes = 0
