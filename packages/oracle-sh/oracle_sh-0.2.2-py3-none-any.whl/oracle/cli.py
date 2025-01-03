import random
from typing import Optional

import typer
from typing_extensions import Annotated

from oracle import __version__
from oracle.display import Display
from oracle.file import File
from oracle.model.group import ChoiceGroup, ChoiceGroupError

app = typer.Typer()
display = Display()
file = File()


@app.callback(invoke_without_command=True, no_args_is_help=True)
def main(
    ctx: typer.Context,
    version: Annotated[Optional[bool], typer.Option("--version")] = False,
) -> None:
    """A pairwise comparer to discover your truth"""
    if version:
        display.diagnostic(f"{__package__} {__version__}")
        typer.Exit()

    if ctx.invoked_subcommand is None:
        pass


@app.command()
def trial() -> None:
    """perform a trial for the current choices"""
    display.success("oracle is determining your fate")

    group = ChoiceGroup.from_json(file.read())
    if len(group) < 2:
        display.confused("oracle cannot guide you")
        raise typer.Exit()

    options = group.get_pair()
    for i, option in enumerate(options):
        display.indexed(i, option.name)
    display.confused("which do you choose?")

    # TODO(mmoran): what if the user types in the option instead of the number
    choice = typer.prompt("[>] 0 or 1?", type=int)

    for i, option in enumerate(options):
        if i == choice:
            option.success()
        else:
            option.trial()

    file.write(group.json)
    display.success("oracle has recorded your choice")


@app.command()
def fate(verbose: Annotated[bool, typer.Option("--verbose")] = False) -> None:
    """reveal the fate of the current choices"""
    display.success("oracle is revealing your fate")

    group = ChoiceGroup.from_json(file.read())
    if len(group) < 2:
        display.confused("oracle cannot guide you")
        raise typer.Exit()

    # TEMP(mmoran): use a weighted random pulling from the choices
    trials = sum(choice.trials for choice in group.choices) // 2
    weights = [
        int(trials * (choice.successes + 1) / (choice.trials + 1)) for choice in group.choices
    ]
    if verbose:
        display.diagnostic(f"options:{[choice.name for choice in group.choices]}")
        display.diagnostic(f"trials:{trials}, weight:{sum(weights)}, weights:{weights}")

    result = random.sample(group.choices, k=1, counts=weights)[0]
    display.success("oracle has determined your fate")
    display.success(result.name)
    # TODO(mmoran): should oracle record the result as a trial?
    # TODO(mmoran): should oracle reset the group after a fate?


@app.command()
def show(verbose: Annotated[bool, typer.Option("--verbose")] = False) -> None:
    """show the active choices"""
    group = ChoiceGroup.from_json(file.read())
    if len(group) == 0:
        display.confused("oracle is waiting for guidance")
        raise typer.Exit()
    elif len(group) == 1:
        display.confused("oracle cannot guide you")
        raise typer.Exit()
    else:
        display.success("oracle is determining your fate")

    for i, choice in enumerate(group.choices):
        details = f" ({choice.successes} / {choice.trials})" if verbose else ""
        message = f"{choice.name}{details}"
        display.indexed(i, message)


@app.command()
def add(name: str) -> None:
    """add a new choice to the available choices"""
    group = ChoiceGroup.from_json(file.read())

    try:
        group.add(name)
    except ChoiceGroupError as e:
        display.confused(str(e))
        raise typer.Exit()

    file.write(group.json)
    display.success("oracle is scrying your new choice")


@app.command()
def remove(name: str) -> None:
    """remove a new choice to the available choices"""
    group = ChoiceGroup.from_json(file.read())

    try:
        group.remove(name)
    except ChoiceGroupError as e:
        display.confused(str(e))
        raise typer.Exit()

    file.write(group.json)
    display.success("oracle has purged your choice")


@app.command()
def reset() -> None:
    """reset the active choices"""
    group = ChoiceGroup.from_json(file.read())
    if len(group) == 0:
        display.confused("oracle is waiting for guidance")
        raise typer.Exit()

    group.reset()

    file.write(group.json)
    display.success("oracle has reset your choices")


if __name__ == "__main__":
    app()
