print('\n\n')

from sys import argv

script, user_name = argv
prompt = '>'  #这个符号随便设置

print("Hi %s,I'm the %s script." % (user_name,script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)  

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright,so you said %s about likeing me.
You live in%s.Not sure where that is .
And you have a %s computer. Nice.
""" %(likes, lives, computer))    # %r改成%s

print('\n\n')
