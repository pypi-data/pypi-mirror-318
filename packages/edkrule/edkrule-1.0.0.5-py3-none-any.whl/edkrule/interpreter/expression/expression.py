import uuid

from edkrule.engine.constant import Constant
from edkrule.engine.engine import Engine
from edkrule.engine.finder.finder import Finder
from edkrule.interpreter.expression.categorize import Categorize
from edkrule.interpreter.lexer.token_type import TokenType
from edkrule.interpreter.lexer.tokens.token import Token


class Expression:
    def __init__(self, body=None):
        if body is None: body = []
        self._body = body
        self._name = None
        self._engine = None
        self.rid = uuid.uuid4().hex
        self._origin_statement = None

    def origin_statement(self, statement):
        self._origin_statement = statement

    def append(self, body):
        self._body.append(body)

    def insert(self, body):
        self._body.insert(0, body)

    @property
    def engine(self) -> Engine:
        return self._engine

    @engine.setter
    def engine(self, value):
        self._engine = value
        for body in self._body:
            if type(body) != Token:
                body.engine = value

    def run(self):
        if self._engine is None: pass
        if self.name == "Anonymous":
            return self.anonymous()
        if self.name == 'TernaryOperator':
            return self.ternary()
        return self.func()

    def func(self):
        runner = self.engine.get_class(Constant.Expressions, self.name)(self.engine, self.rid)
        return runner.run(*[b.run() for b in self._body])

    def anonymous(self):
        if len(self._body) == 1:
            return self._body[0].run()
        else:
            return self.binary()

    def binary(self):
        runner = self.engine.get_class(Constant.Expressions, self._body[1].text)(self.engine, self.rid)
        return runner.run(*[self.body[0].run(), self.body[2].run()])

    def ternary(self):
        if self._body[0].run():
            return self._body[2].run()
        else:
            return self._body[4].run()

    @property
    def type(self):
        return TokenType.Expression

    @property
    def name(self):
        if self._name is None: return "Anonymous"
        return self._name.text

    @name.setter
    def name(self, value):
        self._name = value

    def display2(self, index):
        """
        测试用
        :param index:
        :type index:
        :return:
        :rtype:
        """
        if not index: print(self.name)
        for i, e in enumerate(self._body):
            pos = []
            pos.extend(index)
            pos.append(str(i))
            if Categorize.is_variable(e) or Categorize.is_op(e):
                # exp.matrix(0).name == 'Anonymous'
                print("assert", f'exp.matrix({",".join(pos)}).text == \'{e.text}\'')
                print("assert", f'exp.matrix({",".join(pos)}).type == {e.type}')
            else:
                print("assert", f'exp.matrix({",".join(pos)}).name == \'{e.name}\'')
                print("assert", f'exp.matrix({",".join(pos)}).type == {e.type}')
                # print(",".join(pos), e.name, e.type)
                e.display2(pos)

    def tree_data(self):
        tree_json = dict()
        tree_json["name"] = self.name
        tree_json["children"] = []
        tree_json["value"] = self.text
        tree_json["type"] = "statement"
        for i, e in enumerate(self._body):
            if Categorize.is_variable(e) or Categorize.is_op(e):
                tree_json["children"].append(dict(name=e.text, value=e.text, type=e.type.value))
            else:
                tree_json["children"].append(e.tree_data())
        return tree_json

    def go_tree_data(self, parent_id = None):
        result = []
        tree_json = dict()
        tree_json["name"] = self.text
        tree_json["id"] = str(uuid.uuid4())
        tree_json["gender"] = "F"
        if parent_id: tree_json["parent"] = parent_id
        result.append(tree_json)
        for i, e in enumerate(self._body):
            if e.type == TokenType.Variable:
                result.append(dict(name=e.text, gender="M",parent=tree_json["id"], id=str(uuid.uuid4())))
            elif e.type == TokenType.Expression:
                result.extend(e.go_tree_data(tree_json["id"]))
        return result

    def display(self, level: int = 0, indexes=None):
        """
        测试用
        :param index:
        :type index:
        :return:
        :rtype:
        """
        if indexes is None: indexes = list()
        print(self.name)
        for index, e in enumerate(self._body):
            if Categorize.is_variable(e) or Categorize.is_op(e):
                print(e, e.type, e.text)
            else:
                print(f'{self.blank(level)}------{e.name}-----Start')
                e.display(level + 1, indexes)
                print(f'{self.blank(level)}------{e.name}-----End')

    def blank(self, level):
        return "".join([" " for i in range(level + 1)])

    @property
    def body(self):
        return self._body

    def matrix(self, *args):
        deep = len(args)
        index = 0
        result = self.body[args[index]]
        while deep > 1:
            deep -= 1
            index += 1
            result = result.body[args[index]]
        return result

    def find(self, finder: Finder, finder_parameter):
        return finder.find(self, finder_parameter)

    @property
    def text(self):
        if self._origin_statement is None:
            if len(self.body) == 1 and not self.is_function():
                return self.body[0].text
            if not self.is_function():
                return "".join([e.text for e in self.body])
            else:
                return f"{self.name}({','.join([e.text for e in self.body])})"
        else:
            return self._origin_statement.text

    def is_function(self):
        return self.name != "Anonymous" and self.name != "TernaryOperator"
