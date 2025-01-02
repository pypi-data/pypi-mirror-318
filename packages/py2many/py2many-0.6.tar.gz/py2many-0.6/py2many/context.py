import ast

from .scope import ScopeMixin


def add_list_calls(node):
    """Provide context to Module and Function Def"""
    return ListCallTransformer().visit(node)


def add_variable_context(node, trees):
    """Provide context to Module and Function Def"""
    return VariableTransformer(trees).visit(node)


def add_assignment_context(node):
    """Annotate nodes on the LHS of an assigment"""
    return LHSAnnotationTransformer().visit(node)


class ListCallTransformer(ast.NodeTransformer):
    """
    Adds all calls to list to scope block.
    You need to apply VariableTransformer before you use it.
    """

    def visit_Call(self, node):
        if self.is_list_addition(node):
            var = node.scopes.find(node.func.value.id)
            if var is not None and self.is_list_assignment(var.assigned_from):
                if not hasattr(var, "calls"):
                    var.calls = []
                var.calls.append(node)
        return node

    def is_list_assignment(self, node):
        return (
            hasattr(node, "value")
            and isinstance(node.value, ast.List)
            and hasattr(node, "targets")
            and isinstance(node.targets[0].ctx, ast.Store)
        )

    def is_list_addition(self, node):
        """Check if operation is adding something to a list"""
        list_operations = ["append", "extend", "insert"]
        return (
            hasattr(node.func, "ctx")
            and isinstance(node.func.ctx, ast.Load)
            and hasattr(node.func, "value")
            and isinstance(node.func.value, ast.Name)
            and hasattr(node.func, "attr")
            and node.func.attr in list_operations
        )


class VariableTransformer(ast.NodeTransformer, ScopeMixin):
    """Adds all defined variables to scope block"""

    def __init__(self, trees):
        super().__init__()
        if len(trees) == 1:
            self._trees = {}
        else:
            self._trees = {t.__file__.stem: t for t in trees}

    def visit_FunctionDef(self, node):
        node.vars = []
        # So function signatures are accessible even after they're
        # popped from the scope
        self.scopes[-2].vars.append(node)
        for arg in node.args.args:
            arg.assigned_from = node
            node.vars.append(arg)
        self.generic_visit(node)
        return node

    def visit_ClassDef(self, node):
        node.vars = []
        # So classes are accessible even after they're
        # popped from the scope
        self.scopes[-2].vars.append(node)
        self.generic_visit(node)
        return node

    def visit_Import(self, node):
        for name in node.names:
            name.imported_from = node
        return node

    def visit_ImportFrom(self, node):
        module_path = node.module
        names = [n.name for n in node.names]
        if module_path in self._trees:
            m = self._trees[module_path]
            resolved_names = [m.scopes.find(n) for n in names]
            node.scopes[-1].vars += resolved_names
        return node

    def visit_If(self, node):
        node.vars = []
        self.visit(node.test)
        for e in node.body:
            self.visit(e)
        node.body_vars = node.vars

        node.vars = []
        for e in node.orelse:
            self.visit(e)
        node.orelse_vars = node.vars

        node.vars = []
        return node

    def visit_For(self, node):
        node.target.assigned_from = node
        if isinstance(node.target, ast.Name):
            node.vars = [node.target]
        elif isinstance(node.target, ast.Tuple):
            node.vars = [*node.target.elts]
        else:
            node.vars = []
        self.generic_visit(node)
        return node

    def visit_Module(self, node):
        node.vars = []
        self.generic_visit(node)
        return node

    def visit_With(self, node):
        node.vars = []
        self.generic_visit(node)
        return node

    def visit(self, node):
        with self.enter_scope(node):
            return super().visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                target.assigned_from = node
                self.scope.vars.append(target)
        self.generic_visit(node)
        return node

    def visit_AnnAssign(self, node):
        target = node.target
        if isinstance(target, ast.Name):
            target.assigned_from = node
            self.scope.vars.append(target)
        self.generic_visit(node)
        return node

    def visit_AugAssign(self, node):
        target = node.target
        if isinstance(target, ast.Name):
            target.assigned_from = node
            self.scope.vars.append(target)
        self.generic_visit(node)
        return node


class LHSAnnotationTransformer(ast.NodeTransformer):
    def __init__(self):
        super().__init__()
        self._lhs = False

    def visit(self, node):
        if self._lhs:
            node.lhs = self._lhs
        return super().visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            self._lhs = True
            self.visit(target)
            self._lhs = False
        self.visit(node.value)
        return node

    def visit_AnnAssign(self, node):
        self._lhs = True
        self.visit(node.target)
        self._lhs = False
        self.visit(node.annotation)
        if node.value is not None:
            self.visit(node.value)
        return node

    def visit_AugAssign(self, node):
        self._lhs = True
        self.visit(node.target)
        self._lhs = False
        self.visit(node.op)
        self.visit(node.value)
        return node
