from sys import argv	#引入sys模组
from os.path import exists

script, from_file, to_file = argv	#定义原文件和修改后文件的名称

print("\n\nCopying from %s to %s" %(from_file, to_file) )	#修改变量%s为%r?%d/

#we could do these two on one line.how?
in_file = open(from_file)	#读取原文件内容
indata = in_file.read()		#读取in_file即原文件的内容，用indata表示
print("The input file is %d bytes long" % len(indata) )		#len字节长度

print("Does the ooutput file exist? %r" % exists(to_file) )		#修改后的文件可以自己创建也可以等系统自己创建
print("Ready, hit RETURN to continue, CTRL to abort.")
input()		#python3 与python2不同，python2应该是raw_input

out_file = open(to_file, 'w')	#打开修改文件内容
out_file.write(indata)

print("Alright, all done.\n\n")

out_file.close()	#关闭文件，同下
in_file.close()

#简化
from sys import argv
from os.path import exists
scipt, from_file, to_file = argv
indata = open(from_file).read()
input()
open(to_file,'w').write(indata)