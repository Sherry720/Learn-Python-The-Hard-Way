print('\n\n')    #空两行

from sys import argv    #引入sys模组

script, filename = argv    #得到一个文件，输入文件名
mobi = open(filename)    #定义mobi的功能：打开这个文件； txt改成mobi，下同

print("Here's your file %s:" % filename)    # %r改成%s
print(mobi.read())    #执行文件的read命令（用.紧跟前面）

print("Type the filenaem again:") 
file_again = input(">")    #用>开头（>可替换），然后input输入文件名

mobi_again = open(file_again)

print(mobi_again.read())    #同上

print('\n\n')
