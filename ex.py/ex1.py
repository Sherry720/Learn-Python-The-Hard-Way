print("Hello world!")
print("Hello Again")
print("I like tying this.")
print("This is fun.")
print("Yay!Printing.")
print("I'd much rather you 'not'.")
print("I 'said' do not touch this.")
current_users = ['Bob','Tom','Sherry','admin','Jerry']
for a in current_users[:]:
    a = a.lower()
new_users = ('Jack','Mary','Sherry','admin','John')
for x in new_users[:]:
    if x.lower() in a:  # str.lower()只能直接作用与字符串
        print(x + ',You need to input a another name.')
    else:
        print(x + ",This name is availiable.")
