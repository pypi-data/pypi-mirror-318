import json
import pathlib
from pathlib import Path

from jinja2 import FileSystemLoader, Environment

from edkrule.utils.output.printer import Printer


class PrinterHtml(Printer):



    def output(self, out_path: Path, data, jinja_template_path: Path):
        file_loader = FileSystemLoader(str(jinja_template_path.parent))
        env = Environment(loader=file_loader)

        template = env.get_template(jinja_template_path.name)

        output = template.render(data=data)

        with open(str(out_path), "w", encoding="UTF-8") as f:
            f.write(output)