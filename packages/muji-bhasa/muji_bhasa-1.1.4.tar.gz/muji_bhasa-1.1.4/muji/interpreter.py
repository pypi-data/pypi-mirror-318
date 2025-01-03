# interpreter.py  
  
from muji.parser import Parser  
INTEGER          = 'INTEGER'  
FLOAT            = 'FLOAT'  
PLUS             = 'PLUS'  
MINUS            = 'MINUS'  
MUL              = 'MUL'  
DIV              = 'DIV'  
LPAREN           = 'LPAREN'  
RPAREN           = 'RPAREN'  
IDENTIFIER       = 'IDENTIFIER'  
ASSIGN           = 'ASSIGN'  
SEMI             = 'SEMI'      # Semicolon  
EOF              = 'EOF'       # End-of-file  
INPUT            = 'INPUT'     # van muji  
PRINT            = 'PRINT'     # her muji  
VAR_DECL         = 'VAR_DECL'  # dey muji  
IF               = 'IF'        # yedi muji  
ELIF             = 'ELIF'      # natra bhane muji  
ELSE             = 'ELSE'      # natra muji  
PROGRAM_START    = 'PROGRAM_START'  # oe muji  
PROGRAM_END      = 'PROGRAM_END'    # lala muji  
LBRACE           = 'LBRACE'  
RBRACE           = 'RBRACE'  
EQ               = 'EQ'        # ==  
NE               = 'NE'        # !=  
LT               = 'LT'        # <  
GT               = 'GT'        # >  
LTE              = 'LTE'       # <=  
GTE              = 'GTE'       # >=  
STRING           = 'STRING'  
FOR              = 'FOR'  
WHILE            = 'WHILE'  
  
class NodeVisitor:  
    def visit(self, node):  
        method_name = 'visit_' + type(node).__name__  
        visitor = getattr(self, method_name, self.generic_visit)  
        return visitor(node)  
    def generic_visit(self, node):  
        raise Exception('No visit_{} method'.format(type(node).__name__))  
  
class Interpreter(NodeVisitor):  
    def __init__(self, parser):  
        self.parser = parser  
        self.GLOBAL_MEMORY = {}  

    def visit_String(self, node):  
        return node.value
    
    def visit_BinOp(self, node):  
        left = self.visit(node.left)  
        right = self.visit(node.right)  
        if node.op.type == PLUS:  
            if isinstance(left, str) or isinstance(right, str):  
                return str(left) + str(right)  
            else:  
                return left + right   
        elif node.op.type == MINUS:  
            return left - right  
        elif node.op.type == MUL:  
            return left * right  
        elif node.op.type == DIV:  
            return left / right  
        elif node.op.type in (EQ, NE, LT, GT, LTE, GTE):  
            if node.op.type == EQ:  
                return left == right  
            elif node.op.type == NE:  
                return left != right  
            elif node.op.type == LT:  
                return left < right  
            elif node.op.type == GT:  
                return left > right  
            elif node.op.type == LTE:  
                return left <= right  
            elif node.op.type == GTE:  
                return left >= right  
        else:  
            raise Exception('Unsupported operator')  
          
    def visit_Num(self, node):  
        return node.value  
    def visit_Var(self, node):  
        var_name = node.name  
        value = self.GLOBAL_MEMORY.get(var_name)  
        if value is None:  
            raise Exception(f'Name "{var_name}" is not defined')  
        else:  
            return value  
    def visit_VarDecl(self, node):  
        var_name = node.var_node.name  
        if var_name in self.GLOBAL_MEMORY:  
            raise Exception(f'Variable "{var_name}" is already declared')  
        if node.expr_node is not None:  
            self.GLOBAL_MEMORY[var_name] = self.visit(node.expr_node)  
        else:  
            self.GLOBAL_MEMORY[var_name] = None  # Initialize to None  

    def visit_Assign(self, node):  
        var_name = node.left.name  
        if var_name not in self.GLOBAL_MEMORY:  
            raise Exception(f'Variable "{var_name}" is not declared')  
        self.GLOBAL_MEMORY[var_name] = self.visit(node.right)  
    def visit_Compound(self, node):  
        for child in node.children:  
            self.visit(child)  
    def visit_Print(self, node):  
        value = self.visit(node.expr)  
        print(value)  
    def visit_Input(self, node):  
        var_name = node.var_node.name  
        if var_name not in self.GLOBAL_MEMORY:  
            raise Exception(f'Variable "{var_name}" is not declared')  
        user_input = input()  
        try:  
            value = int(user_input)  
        except ValueError:  
            try:  
                value = float(user_input)  
            except ValueError:  
                value = user_input  # Keep as string if not a number  
        self.GLOBAL_MEMORY[var_name] = value  
    def visit_IfStatement(self, node):  
        executed = False  
        for condition, block in node.cases:  
            if self.visit(condition):  
                self.visit(block)  
                executed = True  
                break  
        if not executed and node.else_block:  
            self.visit(node.else_block)  

    def visit_ForLoop(self, node):  
        # Initialize the loop variable  
        self.visit(node.init)  
        while self.visit(node.condition):  
            # Execute the loop body  
            self.visit(node.body)  
            # Execute the increment statement  
            self.visit(node.increment)  
  
    def visit_WhileLoop(self, node):  
        while self.visit(node.condition):  
            self.visit(node.body)

    def interpret(self):  
        tree = self.parser.parse()  
        self.visit(tree)  