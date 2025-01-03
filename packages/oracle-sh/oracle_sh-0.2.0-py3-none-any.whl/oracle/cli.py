import random
from typing import Callable, Optional

import typer
from typing_extensions import Annotated

from oracle import __version__
from oracle.display import Display
from oracle.file import File
from oracle.model.group import ChoiceGroup

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
        safe_exit(show_version)

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

    choice = typer.prompt("[>]", type=int)

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
    trials = sum(choice.trials for choice in group.choices) // 2 + 1
    counts = [int(trials * choice.successes / (choice.trials + 1)) for choice in group.choices]
    if verbose:
        display.diagnostic(f"options:{[choice.name for choice in group.choices]}")
        display.diagnostic(f"trials:{trials}, total_counts:{sum(counts)}, weights:{counts}")
    result = random.sample(group.choices, k=1, counts=counts)[0]
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
        details = f"({choice.successes}/{choice.trials})" if verbose else ""
        message = f"{choice.name} {details}"
        display.indexed(i, message)


@app.command()
def add(name: str) -> None:
    """add a new choice to the available choices"""
    group = ChoiceGroup.from_json(file.read())

    group.add(name)

    file.write(group.json)
    display.success("oracle is scrying your new choice")


@app.command()
def reset() -> None:
    """reset the active choices"""
    group = ChoiceGroup.from_json(file.read())

    group.reset()

    file.write(group.json)
    display.success("oracle has reset your choices")


def safe_exit(callable: Callable, *args) -> None:
    try:
        callable(*args)
    except Exception as e:
        raise typer.Exit()


def show_version() -> None:
    display.diagnostic(f"{__package__} {__version__}")


if __name__ == "__main__":
    app()
