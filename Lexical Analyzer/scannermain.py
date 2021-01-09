import scannerclass as sc
import scannerfunc as sf

file_name = './test.txt'
scanner = sf.scanner(file_name)

#打印测试文本
with open(file_name) as f:
    print('测试文本内容：')
    print('===================================================')
    print(f.read())
    print('===================================================')

#词法分析过程
if scanner.fp != None:
    print('\n词法分析过程：')
    print('       记号类别                字符串       常数值')
    print('===================================================')
    while(1):
        token = scanner.GetToken()  #输出一个记号
        if token.Type == sc.Token_Type.END: #读到结束符号
            print('===================================================')
            break
        else:
            print("{:25s},{:>10s},{:12f}".format(token.Type, token.lexeme,token.value))
else:
    print('\nOpen Error!')

#打印关键字表
print('\n关键字表：')
print('  关键字              指针')
print('===================================================')
for key,value in sc.Key.items():
    print("{:8s},{:>12s}".format(key,str(value)))
print('===================================================')

#打印并保存标识符表
open("./Alphabet.txt", 'w').close()
with open('./Alphabet.txt','a') as f:
    print('\n标识符表：')
    print('  标识符              指针')
    print('===================================================')
    for key,value in sc.Alphabet.items():
        print("{:8s},{:>12s}".format(key,str(value)))
        f.write("{:8s},{:>12s}\n".format(key,str(value)))
    print('===================================================')

#打印并保存常数表
open("./Const.txt", 'w').close()
with open('./Const.txt','a') as f:
    print('\n常数表：')
    print('  常数              指针')
    print('===================================================')
    for key,value in sc.Const.items():
        print("{:8s},{:>12s}".format(key,str(value)))
        f.write("{:8s},{:>12s}\n".format(key,str(value)))
    print('===================================================')
