from io import StringIO
from pathlib import Path

from edkrule.engine.engine import Engine
from edkrule.engine.result import Result
from edkrule.interpreter.expression.interpreter import Interpreter
from edkrule.interpreter.lexer.lexer import Lexer
from edkrule.interpreter.parse.parser import Parser
from edkrule.utils.output.by import By
from edkrule.utils.rule_show import RuleShow


# TODO 导出 语法路径 HTML
# TODO 规则阅读器 APP
# TODO 词法解析的时候，不应该把Math.power()的形式解析成Math.power, ( , )
# TODO 这种函数的判断应该放在语法分析
# TODO 支持正则表达式
class EdkRule:
    @staticmethod
    def lexer(rule_string: str):
        """
        返回规则词法分析的结果
        :param rule_string:
        :type rule_string:
        :return:
        :rtype:
        """
        l = Lexer()
        l.tokenize(StringIO(rule_string))
        return l.token_list

    @staticmethod
    def parser(rule_string: str):
        """
        返回规则语法分析的结果
        :param rule_string:
        :type rule_string:
        :return:
        :rtype:
        """
        es = Parser(EdkRule.lexer(rule_string))
        es.parse()
        return es.statement

    @staticmethod
    def expression(rule_string: str):
        """
        返回规则表达式分析的结果
        :param rule_string:
        :type rule_string:
        :return:
        :rtype:
        """
        statement = EdkRule.parser(rule_string)
        exp = Interpreter().interpret(statement)
        exp.origin_statement(statement)
        return exp

    @staticmethod
    def run(rule_string: str, engine_path: str = "", use_sys=True, none_default = False) -> Result:
        """
        运行规则
        传参方式 1.
            engine_path = “” and use_sys=True 只是用系统默认规则引擎
        传参方式 2.
            engine_path = “xxxxx” and use_sys=True 同时加载传入的引擎配置和系统默认规则引擎
            如果有相同的名字的，加载传入的引擎配置会覆盖系统默认的配置
        传参方式 3.
            engine_path = “xxxxx” and use_sys=False 只加载传入的引擎配置
        :param rule_string: 规则字符串
        :type rule_string:
        :param engine_path: 加载的 引擎配置的 XML 路径
        :type engine_path:
        :param use_sys: 是否加载系统默认的规则
        :type use_sys:
        :return:
        :rtype:
        """
        try:
            engine = Engine(definition_path=engine_path, use_sys=use_sys)
            rule = EdkRule.expression(rule_string)
            rule.engine = engine
            rule.run()
            return Result(rule)
        except Exception as e:
            if none_default: return None
            raise e

    @staticmethod
    def draw(rule_string: str, output_path: Path):
        """
        画出规则的语法树
        :param rule_string:
        :type rule_string:
        :param output_path:
        :type output_path:
        :return:
        :rtype:
        """
        expression = EdkRule.expression(rule_string)
        data = expression.tree_data()

        RuleShow().output(By.Html, output_path, data)