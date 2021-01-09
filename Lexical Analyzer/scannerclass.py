from enum import Enum
import math

Token_Type = Enum('Token_Type', ('IF', 'ELSE',   #保留字
                                 'SEMICO', 'L_BRACKET','R_BRACKET','L_BRACE','R_BRACE', #分隔符
                                 'LOW', 'GREAT', 'EQ', 'NEQ', 'LEQ', 'GEQ',
                                 'PLUS','MINUS','MUL','DIV','POWER',    #运算符
                                 'DEF', #赋值符
                                 'IDENTIFIER',  #标识符
                                 'CONST',    #常数
                                 'END',    #结束符
                                 'ERRTOKEN'))   #出错记号

class Tokens:   #记号类
    #Type：记号类别
    #lexeme：输入的字符串/属性
    #value：常数值
    def __init__(self,Type,lexeme,value):
        self.lexeme=lexeme
        self.value=value
        if Type in Token_Type:
            self.Type = Type
        else:
            print("Invalid Type")     # 后续待填充

Key=dict([('IF',Tokens(Token_Type.IF,"IF",0.0)),
          ('ELSE',Tokens(Token_Type.ELSE,"ELSE",0.0))])
Alphabet=dict([])
Const=dict([])
