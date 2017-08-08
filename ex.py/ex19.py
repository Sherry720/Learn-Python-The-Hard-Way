def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print("\nYou have %d cheeses!" % cheese_count)
	print("You have %d boses of crackers!" % boxes_of_crackers)
	print("Man that's enough for a party!")
	print("Get a blanet.\n")
	
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can use varibles from our scipt:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, varibles and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def god(god1, god2):
	print("\ngod1 is %d" % god1)
	print("god2 is %d" % god2)
god(12,450)
god(666 + 23333, 555-9)
god1 = god2 = 666
god(god1 + 4321, god2/4)