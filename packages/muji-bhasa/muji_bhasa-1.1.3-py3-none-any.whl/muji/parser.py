# parser.py  
  
from muji.lexer import Token, Lexer  
from muji.token_types import *  
  
class AST:  
    pass  
  
class BinOp(AST):  
    def __init__(self, left, op, right):  
        self.left = left  
        self.op = op  
        self.right = right  
  
class Num(AST):  
    def __init__(self, token):  
        self.token = token  
        self.value = token.value  
  
class Var(AST):  
    def __init__(self, token):  
        self.token = token  
        self.name = token.value  
  
class Assign(AST):  
    def __init__(self, left, op, right):  
        self.left = left  # Var  
        self.op = op      # Token(ASSIGN)  
        self.right = right  
  
class VarDecl(AST):  
    def __init__(self, var_node, expr_node):  
        self.var_node = var_node  
        self.expr_node = expr_node  
  
class Compound(AST):  
    def __init__(self):  
        self.children = []  
  
class Print(AST):  
    def __init__(self, expr):  
        self.expr = expr  
  
class Input(AST):  
    def __init__(self, var_node):  
        self.var_node = var_node  
  
class IfStatement(AST):  
    def __init__(self):  
        self.cases = []  # List of tuples (condition, block)  
        self.else_block = None  

class String(AST):  
    def __init__(self, token):  
        self.token = token  
        self.value = token.value  

class ForLoop(AST):  
    def __init__(self, init, condition, increment, body):  
        self.init = init          # Initialization statement  
        self.condition = condition  
        self.increment = increment  
        self.body = body  
  
class WhileLoop(AST):  
    def __init__(self, condition, body):  
        self.condition = condition  
        self.body = body 
  
class Parser:  
    def __init__(self, lexer):  
        self.lexer = lexer  
        self.current_token = self.lexer.get_next_token()  
        self.peek_token = self.lexer.get_next_token()  
    def error(self):  
        raise Exception('Invalid syntax')  
    def eat(self, token_type):  
        if self.current_token.type == token_type:  
            self.current_token = self.peek_token  
            self.peek_token = self.lexer.get_next_token()  
        else:  
            self.error()  
    def factor(self):  
        token = self.current_token  
        if token.type in (PLUS, MINUS):  
            self.eat(token.type)  
            node = self.factor()  
            return BinOp(left=Num(Token(INTEGER, 0)), op=token, right=node)  
        elif token.type in (INTEGER, FLOAT):  
            self.eat(token.type)  
            return Num(token)  
        elif token.type == IDENTIFIER:  
            self.eat(IDENTIFIER)  
            return Var(token)  
        elif token.type == STRING:  
            self.eat(STRING)  
            return String(token)  
        elif token.type == LPAREN:  
            self.eat(LPAREN)  
            node = self.expr()  
            self.eat(RPAREN)  
            return node  
        else:  
            self.error()   
    def term(self):  
        node = self.factor()  
        while self.current_token.type in (MUL, DIV):  
            token = self.current_token  
            self.eat(token.type)  
            node = BinOp(left=node, op=token, right=self.factor())  
        return node  
    def expr(self):  
        node = self.term()  
        while self.current_token.type in (PLUS, MINUS):  
            token = self.current_token  
            self.eat(token.type)  
            node = BinOp(left=node, op=token, right=self.term())  
        return node  
    def comparison(self):  
        node = self.expr()  
        while self.current_token.type in (EQ, NE, LT, GT, LTE, GTE):  
            token = self.current_token  
            self.eat(token.type)  
            node = BinOp(left=node, op=token, right=self.expr())  
        return node  
    def variable_declaration(self):  
        self.eat(VAR_DECL)  # dey muji  
        var_node = Var(self.current_token)  
        self.eat(IDENTIFIER)  
        expr_node = None  
        if self.current_token.type == ASSIGN:  
            self.eat(ASSIGN)  
            expr_node = self.expr()  
        self.eat(SEMI)  
        node = VarDecl(var_node, expr_node)  
        return node  
    def assignment(self):  
        var_node = Var(self.current_token)  
        self.eat(IDENTIFIER)  
        self.eat(ASSIGN)  
        expr_node = self.expr()  
        self.eat(SEMI)  
        node = Assign(var_node, Token(ASSIGN, '='), expr_node)  
        return node  
    def print_statement(self):  
        self.eat(PRINT)  # her muji  
        expr = self.expr()  
        self.eat(SEMI)  
        return Print(expr)  
    def input_statement(self):  
        self.eat(INPUT)  # van muji  
        var_node = Var(self.current_token)  
        self.eat(IDENTIFIER)  
        self.eat(SEMI)  
        return Input(var_node)  
    def if_statement(self):  
        node = IfStatement()  
        self.eat(IF)  # yedi muji  
        condition = self.comparison()  
        self.eat(LBRACE)  
        block = self.statement_list()  
        self.eat(RBRACE)  
        node.cases.append((condition, block))  
        while self.current_token.type == ELIF:  
            self.eat(ELIF)  # natra bhane muji now corresponds to ELIF  
            condition = self.comparison()  
            self.eat(LBRACE)  
            block = self.statement_list()  
            self.eat(RBRACE)  
            node.cases.append((condition, block))  
        if self.current_token.type == ELSE:  
            self.eat(ELSE)  # natra muji now corresponds to ELSE  
            self.eat(LBRACE)  
            node.else_block = self.statement_list()  
            self.eat(RBRACE)  
        return node  
    
    def for_loop(self):  
        self.eat(FOR)  # gardai gar muji  
        self.eat(LPAREN)  
        init = self.statement()  
        condition = self.comparison()  
        self.eat(SEMI)  
        increment = self.statement()  
        self.eat(RPAREN)  
        self.eat(LBRACE)  
        body = self.statement_list()  
        self.eat(RBRACE)  
        node = ForLoop(init, condition, increment, body)  
        return node  
  
    def while_loop(self):  
        self.eat(WHILE)  # jaba samma muji  
        condition = self.comparison()  
        self.eat(LBRACE)  
        body = self.statement_list()  
        self.eat(RBRACE)  
        node = WhileLoop(condition, body)  
        return node 
    
    def statement(self):  
        if self.current_token.type == VAR_DECL:  
            node = self.variable_declaration()  
        elif self.current_token.type == IDENTIFIER and self.peek_token.type == ASSIGN:  
            node = self.assignment()  
        elif self.current_token.type == PRINT:  
            node = self.print_statement()  
        elif self.current_token.type == INPUT:  
            node = self.input_statement()  
        elif self.current_token.type == IF:  
            node = self.if_statement()  
        elif self.current_token.type == FOR:  
            node = self.for_loop()  
        elif self.current_token.type == WHILE:  
            node = self.while_loop()  
        else:  
            self.error()  
        return node  
    
    def statement_list(self):  
        nodes = []  
        while self.current_token.type != EOF and self.current_token.type != RBRACE and self.current_token.type != PROGRAM_END:  
            node = self.statement()  
            nodes.append(node)  
        compound = Compound()  
        compound.children = nodes  
        return compound  
    def program(self):  
        self.eat(PROGRAM_START)  
        node = self.statement_list()  
        self.eat(PROGRAM_END)  
        if self.current_token.type != EOF:  
            self.error()  
        return node  
    def parse(self):  
        return self.program()  