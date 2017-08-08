print('\n\n')    #空两行

from sys import argv    #引入sys模组

script, filename = argv    #得到一个文件，输入文件名

print("We're going to erase %s." % filename)	#括号内意思是擦除这个文件
print("If you don't want that,hit CTRL-C (^C).")	#具体步骤说明
print("If you want that,hit RETURN.")	#同上

input("?\n")	

print("Opening the file...")
target = open(filename,'w')		# 'w'是write

print("Truncating the file.	Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")	#输入三句话，同下
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write("%s\n%s\n%s\n" %(line1,line2,line3))	#写入文件，指令target
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")	#不同写入方法


print("And finally, we close it.")
target.close()	#关闭文件