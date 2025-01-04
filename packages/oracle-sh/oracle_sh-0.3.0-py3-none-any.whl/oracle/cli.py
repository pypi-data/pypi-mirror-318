import random
from typing import Optional

import typer
from typing_extensions import Annotated

from oracle import __version__
from oracle.controller import Controller
from oracle.display import Display
from oracle.file import File
from oracle.model.group import ChoiceGroup, ChoiceGroupError

app = typer.Typer()
display = Display()
file = File()
controller = Controller(file, display)


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
    controller.refresh()
    group = controller.group

    if len(group) < 2:
        display.warning("oracle cannot guide you")
        display.confused("oracle needs to be aware of more possibilities for your future")
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

    controller.save()
    display.success("oracle has recorded your choice")


@app.command()
def fate(
    verbose: Annotated[bool, typer.Option("--verbose")] = False,
    final: Annotated[bool, typer.Option("--final")] = False,
) -> None:
    """reveal the fate of the current choices"""
    display.success("oracle is revealing your fate")
    controller.refresh()
    group = controller.group

    if len(group) < 2:
        display.warning("oracle cannot guide you")
        display.confused("oracle needs to be aware of more possibilities for your future")
        raise typer.Exit()

    # TEMP(mmoran): use a weighted random pulling from the choices
    trials = sum(choice.trials for choice in group.choices) // 2
    if trials == 0:
        display.warning("oracle cannot guide you")
        display.confused("oracle has not scryed your future")
        raise typer.Exit()

    weights = [
        int((choice.successes + 1) * (choice.trials + 1) / trials) for choice in group.choices
    ]
    if verbose:
        display.diagnostic(f"options:{[choice.name for choice in group.choices]}")
        display.diagnostic(f"trials:{trials}, weight:{sum(weights)}, weights:{weights}")

    result = random.sample(group.choices, k=1, counts=weights)[0]
    display.success("oracle has determined your fate")
    display.info(f"oracle has chosen '{result.name}' as your future")

    if final:
        group.reset()
        controller.save()
        display.success("oracle is waiting for guidance")
    # TODO(mmoran): should oracle record the result as a trial?


@app.command()
def show(verbose: Annotated[bool, typer.Option("--verbose")] = False) -> None:
    """show the active choices"""
    controller.refresh()
    group = controller.group

    if len(group) == 0:
        display.confused("oracle is waiting for guidance")
        raise typer.Exit()

    display.success("oracle is determining your fate")
    for choice in group.choices:
        details = f" ({choice.successes}/{choice.trials})" if verbose else ""
        message = f"{choice.name}{details}"
        display.info(message)


@app.command()
def add(name: str) -> None:
    """add a new choice to the available choices"""
    controller.refresh()
    group = controller.group

    try:
        group.add(name)
    except ChoiceGroupError as e:
        display.confused(str(e))
        raise typer.Exit()

    controller.save()
    display.success("oracle is scrying your new choice")


@app.command()
def remove(name: str) -> None:
    """remove a new choice to the available choices"""
    controller.refresh()
    group = controller.group

    try:
        group.remove(name)
    except ChoiceGroupError as e:
        display.confused(str(e))
        raise typer.Exit()

    controller.save()
    display.success("oracle has purged your choice")


@app.command()
def reset() -> None:
    """reset the active choices"""
    controller.refresh()
    group = controller.group

    if len(group) == 0:
        display.confused("oracle is waiting for guidance")
        raise typer.Exit()

    group.reset()

    controller.save()
    display.success("oracle has reset your choices")


@app.command()
def clear() -> None:
    """clear all saved information"""
    controller.refresh()
    controller.group = ChoiceGroup()
    controller.save()
    display.success("oracle has forgotten everything")


if __name__ == "__main__":
    app()
