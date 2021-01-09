import scannerclass as sc
import os


class scanner():

    ##——————初始化词法分析器
    def __init__(self,file_name):   #输入要输入字符流的文件名
        self.TokenBuffer = '' #待识别记号缓存区
        self.file_name=file_name
        if os.path.exists(self.file_name):
            self.fp = open(self.file_name, "r")     #文件指针
        else:
            self.fp = None

    ##——————关闭词法分析器
    def CloseScanner(self):
        if self.fp!=None:
            self.fp.close()

    ##——————从输入流中读入一个字符
    def GetChar(self):
        Char = self.fp.read(1)
        return Char

    ##——————输入流回退一个字符
    def BackChar(self,Char):        ## 非二进制打开方式不能直接seek目前位置回溯，所以用tell()-1方式从头跳转前一位置
        if Char != '':
            self.fp.seek(self.fp.tell()-1)

    ##——————加入字符到TokenBuffer待识别字符串中
    def AddCharToString(self,Char):
        self.TokenBuffer+=Char

    ##——————清空TokenBuffer字符串
    def EmptyString(self):
        self.TokenBuffer=''

    ##——————识别的字符串查关键字表和标识符表
    def JudgeKeyAlphabet(self):
        # 查关键字表
        Token=sc.Key.get(self.TokenBuffer,sc.Tokens(sc.Token_Type.ERRTOKEN,self.TokenBuffer,0.0))
        if Token.Type == sc.Token_Type.ERRTOKEN: #不在关键字表，查标识符表
            Token=sc.Alphabet.get(self.TokenBuffer,sc.Tokens(sc.Token_Type.IDENTIFIER,self.TokenBuffer,0.0))
            sc.Alphabet[self.TokenBuffer] = Token #不在标识符表中，添加新的项
        return Token

    ##——————识别的常数查常数表
    def JudgeConst(self):
        Token=sc.Const.get(self.TokenBuffer,sc.Tokens(sc.Token_Type.CONST,self.TokenBuffer,float(self.TokenBuffer)))
        sc.Const[self.TokenBuffer] = Token #不在常数表中，添加新的项
        return Token

    ##——————获取记号
    # 每调用该函数一次，仅仅获得一个记号。
    # 为获得源程序的所有记号，就要重复调用这个函数。
    # 输出一个记号，没有输入
    def GetToken(self):

        Char = ''   ##字符流
        pointer = ''   ##指向返回输出的Tokens对象
        self.EmptyString()  #清空缓冲区
        
        Char = self.GetChar()
        while(Char == ' ' or Char == '\n' or Char == '\t'):
            Char = self.GetChar()
        self.AddCharToString(Char) ##若不是空格、TAB、回车、文件结束符等，则先加入到记号的字符缓冲区中
        
        if Char.isalpha():## 判断是否是英文
            while(1):
                Char = self.GetChar()
                if Char.isalnum():
                    self.AddCharToString(Char)
                else:
                    break
            self.BackChar(Char)
            pointer = self.JudgeKeyAlphabet()
            pointer.lexeme = self.TokenBuffer
            return pointer

        elif Char.isdigit():
            while(1):
                Char = self.GetChar()
                if Char.isdigit():
                    self.AddCharToString(Char)
                else:
                    break
            if Char == '.':
                self.AddCharToString(Char)
                while(1):
                    Char = self.GetChar()
                    if Char.isdigit():
                        self.AddCharToString(Char)
                    else:
                        break
            self.BackChar(Char)
            pointer = self.JudgeConst()
            pointer.lexeme = self.TokenBuffer
            return pointer

        else:
            if Char == ';':
                pointer = sc.Tokens(sc.Token_Type.SEMICO,';',0.0)
            elif Char == '(':
                pointer = sc.Tokens(sc.Token_Type.L_BRACKET,'(',0.0)
            elif Char == ')':
                pointer = sc.Tokens(sc.Token_Type.R_BRACKET, ')', 0.0)
            elif Char == '{':
                pointer = sc.Tokens(sc.Token_Type.L_BRACE,'{',0.0)
            elif Char == '}':
                pointer = sc.Tokens(sc.Token_Type.L_BRACE,'}',0.0)
                
            elif Char == '=':   ##可能是赋值符号或比较符号
                Char = self.GetChar()
                if (Char == '='):
                        pointer = sc.Tokens(sc.Token_Type.EQ, '==', 0.0)
                else:
                    self.BackChar(Char)
                    pointer = sc.Tokens(sc.Token_Type.DEF,'=',0.0)
            elif Char == '>':
                Char = self.GetChar()
                if (Char == '='):
                        pointer = sc.Tokens(sc.Token_Type.GEQ, '>=', 0.0)
                else:
                    self.BackChar(Char)
                    pointer = sc.Tokens(sc.Token_Type.GREAT,'>',0.0)
            elif Char == '<':
                Char = self.GetChar()
                if (Char == '='):
                        pointer = sc.Tokens(sc.Token_Type.LEQ, '<=', 0.0)
                else:
                    self.BackChar(Char)
                    pointer = sc.Tokens(sc.Token_Type.LOW,'<',0.0)
            elif Char == '!':
                Char = self.GetChar()
                if (Char == '='):
                        pointer = sc.Tokens(sc.Token_Type.NEQ, '!=', 0.0)
                else:
                    self.BackChar(Char)
                    pointer = sc.Tokens(sc.Token_Type.ERRTOKEN, '!', 0.0)
                    
            elif Char == '+':
                pointer = sc.Tokens(sc.Token_Type.PLUS, '+', 0.0)
            elif Char == '-':
                pointer = sc.Tokens(sc.Token_Type.MINUS, '-', 0.0)
            elif Char == '/':
                pointer = sc.Tokens(sc.Token_Type.DIV, '/', 0.0)
            elif Char == '*':   ##可能是幂运算符或乘号
                Char = self.GetChar()
                if (Char == '*'):
                        pointer = sc.Tokens(sc.Token_Type.POWER, '**', 0.0)
                else:
                    self.BackChar(Char)
                    pointer = sc.Tokens(sc.Token_Type.MUL, '*', 0.0)
            elif Char == '#':
                pointer = sc.Tokens(sc.Token_Type.END,'#',0.0)
            else:
                pointer = sc.Tokens(sc.Token_Type.ERRTOKEN, Char, 0.0) 
        return pointer

