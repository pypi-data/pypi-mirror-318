import abc
import pathlib
from pathlib import Path


class Printer(abc.ABC):
    @staticmethod
    def default_jinja_template():
        return pathlib.Path(__file__).parent.joinpath(pathlib.Path("tree-vertical.html.jinja"))

    @abc.abstractmethod
    def output(self, out_path: Path, data, output_format): ...