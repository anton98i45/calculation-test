import ast
from api.models import CalculationLog
from typing import Any
import operator


class CalculationService:
    def _eval_node(self, node):
        if isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            op = {
                ast.Add: operator.add,
                ast.Sub: operator.sub,
                ast.Mult: operator.mul,
                ast.Div: operator.truediv,
            }
            return op[type(node.op)](left, right)
        elif isinstance(node, ast.Num):
            return node.n
        else:
            raise TypeError(node)

    def safe_eval_expression(self, expr: str) -> tuple[str, Any]:
        result = None
        error = None
        try:
            tree = ast.parse(expr, mode="eval")
            result = self._eval_node(tree.body)
            CalculationLog.objects.create(expression=expr, result=result)
        except Exception as e:
            error = f"Error in calculation: {e}"
        return (result, error)
