# lexer.py  
  
import re  
from token_types import *  
  
class Token:  
    def __init__(self, type_, value):  
        self.type = type_  
        self.value = value  
    def __repr__(self):  
        return f'Token({self.type}, {repr(self.value)})'  
  
class Lexer:  
    def __init__(self, text):  
        self.text = text  
        self.pos = 0  
        self.current_char = self.text[self.pos] if self.text else None  
    def advance(self):  
        self.pos += 1  
        if self.pos >= len(self.text):  
            self.current_char = None  
        else:  
            self.current_char = self.text[self.pos]  
    def skip_whitespace(self):  
        while self.current_char is not None and self.current_char.isspace():  
            self.advance()  
    def peek(self, length):  
        peek_pos = self.pos  
        chars = ''  
        for _ in range(length):  
            if peek_pos >= len(self.text):  
                break  
            chars += self.text[peek_pos]  
            peek_pos += 1  
        return chars  
    def match_keyword(self, keywords):  
        for keyword, token_type in keywords.items():  
            length = len(keyword)  
            if self.peek(length) == keyword:  
                for _ in range(length):  
                    self.advance()  
                return Token(token_type, keyword)  
        return None
    def number(self):  
        result = ''  
        has_dot = False  
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):  
            if self.current_char == '.':  
                if has_dot:  
                    break  
                has_dot = True  
            result += self.current_char  
            self.advance()  
        if has_dot:  
            return Token(FLOAT, float(result))  
        else:  
            return Token(INTEGER, int(result))  
    def identifier(self):  
        result = ''  
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):  
            result += self.current_char  
            self.advance()  
        return Token(IDENTIFIER, result)  
    
    def string(self):  
        result = ''  
        self.advance()  # Skip the opening quote  
        while self.current_char is not None and self.current_char != '"':  
            result += self.current_char  
            self.advance()  
        if self.current_char == '"':  
            self.advance()  # Skip the closing quote  
            return Token(STRING, result)  
        else:  
            raise Exception('Unterminated string literal')
        
    def get_next_token(self):  
        while self.current_char is not None:  
            if self.current_char.isspace():  
                self.skip_whitespace()  
                continue  
            # Match multi-word keywords  
            keywords = {  
            'oe muji': PROGRAM_START,  
            'lala muji': PROGRAM_END,  
            'van muji': INPUT,  
            'her muji': PRINT,  
            'dey muji': VAR_DECL,  
            'yedi muji': IF,  
            'natra bhane muji': ELIF,  # Now ELIF  
            'natra muji': ELSE,        # Now ELSE  
            'gardai gar muji': FOR,  
            'jaba samma muji': WHILE  
        } 
            token = self.match_keyword(keywords)  
            if token:  
                return token  
            if self.current_char == '"':  
                return self.string()
            if self.current_char.isdigit():  
                return self.number()  
            if self.current_char.isalpha() or self.current_char == '_':  
                return self.identifier()  
            if self.current_char == '+':  
                self.advance()  
                return Token(PLUS, '+')  
            if self.current_char == '-':  
                self.advance()  
                return Token(MINUS, '-')  
            if self.current_char == '*':  
                self.advance()  
                return Token(MUL, '*')  
            if self.current_char == '/':  
                self.advance()  
                return Token(DIV, '/')  
            if self.current_char == '(':  
                self.advance()  
                return Token(LPAREN, '(')  
            if self.current_char == ')':  
                self.advance()  
                return Token(RPAREN, ')')  
            if self.current_char == '{':  
                self.advance()  
                return Token(LBRACE, '{')  
            if self.current_char == '}':  
                self.advance()  
                return Token(RBRACE, '}')  
            if self.current_char == ';':  
                self.advance()  
                return Token(SEMI, ';')  
            if self.current_char == '=':  
                self.advance()  
                if self.current_char == '=':  
                    self.advance()  
                    return Token(EQ, '==')  
                else:  
                    return Token(ASSIGN, '=')  
            if self.current_char == '!':  
                self.advance()  
                if self.current_char == '=':  
                    self.advance()  
                    return Token(NE, '!=')  
                else:  
                    raise Exception('Invalid character: !')  
            if self.current_char == '<':  
                self.advance()  
                if self.current_char == '=':  
                    self.advance()  
                    return Token(LTE, '<=')  
                else:  
                    return Token(LT, '<')  
            if self.current_char == '>':  
                self.advance()  
                if self.current_char == '=':  
                    self.advance()  
                    return Token(GTE, '>=')  
                else:  
                    return Token(GT, '>')  
            raise Exception(f'Invalid character: {self.current_char}')  
        return Token(EOF, None)  