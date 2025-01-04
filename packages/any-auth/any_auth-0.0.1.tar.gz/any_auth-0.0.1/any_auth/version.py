import pathlib
import typing


def get_version() -> typing.Text:
    return pathlib.Path(__file__).parent.joinpath("VERSION").read_text().strip()
