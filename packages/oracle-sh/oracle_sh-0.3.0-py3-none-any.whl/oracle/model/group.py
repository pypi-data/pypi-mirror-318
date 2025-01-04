from dataclasses import field
import random
from typing import List

from pydantic import BaseModel

from oracle.model.choice import Choice


class ChoiceGroup(BaseModel):
    name: str = "oracle"
    choices: List[Choice] = field(default_factory=list)

    def __len__(self) -> int:
        return len(self.choices)

    def add(self, name: str, trials: int = 0, successes: int = 0) -> None:
        current_choices = [choice.name for choice in self.choices]
        if name in current_choices:
            raise ChoiceGroupError(f"{name} is already a choice")
        self.choices.append(Choice(name=name, trials=trials, successes=successes))

    def remove(self, name: str) -> None:
        for i, choice in enumerate(self.choices):
            if name == choice.name:
                del self.choices[i]
                break
        else:
            raise ChoiceGroupError(f"{name} is not a choice")

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
