from dataclasses import field
import uuid

from pydantic import UUID4, BaseModel


class Choice(BaseModel):
    name: str
    trials: int = 0
    successes: int = 0
    id: UUID4 = field(default_factory=uuid.uuid4)

    def __hash__(self) -> int:
        return hash(self.id)

    def __str__(self) -> str:
        return self.name

    def trial(self) -> None:
        self.trials += 1

    def success(self) -> None:
        self.trials += 1
        self.successes += 1

    def reset(self) -> None:
        self.trials = 0
        self.successes = 0


class ChoiceError(Exception):
    pass
