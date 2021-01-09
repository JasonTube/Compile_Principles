Writen by：Jinyang Jiang, WHU

Introduction：
这是一个小语言的词法分析程序，因为只做词法分析就没有处理一些二义性的问题，语言的文法是
S->	A#
A->	(B|C)*
B->	IF(D){C}
	|IF(D){C}ELSE{C}
C->	id=E;
	|epsilon
D->	F>F
	|F<F
	|F==F
	|F>=F
	|F<=F
	|F!=F
E->	E+E
	|E-E
	|E*E
	|E/E
	|-E
	|E**E
	|(E)
	|F
F->	id
	|const
id->	(a|...|Z|0|...|9)+
const->	(1|...|9)(0|...|9)*
	|(1|...|9)(0|...|9)*.(0|...|9)+
	|0.(0|...|9)+

scannerclass.py：内含串类的枚举定义、Tokens数据结构的定义和关键字表、标识符表、常数表的定义
scannerfunc.py：词法分析器类
scannermain.py：主程序，运行时打印测试文本、打印词法分析过程、打印并保存标识符表和常数表

test.txt：测试文本
Alphabet.txt：标识符表输出，两栏分别为标识符名和指针
Const.txt：常数表输出，两栏分别为常数和指针