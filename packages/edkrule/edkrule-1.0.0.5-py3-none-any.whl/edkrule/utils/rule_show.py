from pathlib import Path

# from edkrule.edk_rule import EdkRule
from edkrule.utils.output.printer import Printer


class RuleShow:
    # def __init__(self, rule_string: str):
    #     self._expression = EdkRule().expression(rule_string)

    def output(self, printer: Printer, output_path, data):
        printer.output(output_path, data, Printer.default_jinja_template())
