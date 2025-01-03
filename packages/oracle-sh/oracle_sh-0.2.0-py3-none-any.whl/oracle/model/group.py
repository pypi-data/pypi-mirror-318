from dataclasses import asdict, dataclass, field
import random
from typing import List

from oracle.model.choice import Choice


@dataclass
class ChoiceGroup:
    name: str
    choices: List[Choice] = field(default_factory=list)

    def __len__(self) -> int:
        return len(self.choices)

    @property
    def json(self) -> dict:
        return asdict(self)

    @classmethod
    def from_json(cls, data: dict) -> "ChoiceGroup":
        group = ChoiceGroup(data["name"])
        for choice in data["choices"]:
            group.choices.append(Choice(**choice))
        return group

    def add(self, name: str) -> None:
        # TODO(mmoran): check for duplicates
        self.choices.append(Choice(name))

    def remove(self, name: str) -> None:
        for i, choice in enumerate(self.choices):
            if name == choice.name:
                del self.choices[i]
                break

    def reset(self) -> None:
        for choice in self.choices:
            choice.reset()

    def get_pair(self) -> tuple[Choice, Choice]:
        if len(self) < 2:
            raise ChoiceGroupError("not enough choices to make a pair")

        first_idx, second_idx = 0, 0
        while first_idx == second_idx:
            first_idx, second_idx = random.sample(range(len(self)), k=2)
        return self.choices[first_idx], self.choices[second_idx]


class ChoiceGroupError(Exception):
    pass
