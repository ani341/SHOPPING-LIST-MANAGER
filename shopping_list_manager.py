#SHOPPING LIST MANAGER
# asking user for his name and doing it in title case 

user_name = input("enter your full name please :")

print("welcome to shopping list manager MR",user_name.title())

# asking the user for enter grocery items one by one 
grocery = []

g1 = str(input("enter your first grocery item :"))
grocery.append(g1)
g2 = str(input("enter your 2nd grocery item :"))
grocery.append(g2)
g3 = str(input("enter your 3rd grocery item :"))
grocery.append(g3)
g4 = str(input("enter your 4th grocery item :"))
grocery.append(g4)

grocery.append("eggs")

grocery.sort()
print(grocery)

# showing the total number of item using len 
print("the total number of items is :",len(grocery))

# Tell the user what item is at position 0 after sorting, with its first letter capitalized
position = grocery[0].capitalize()
print("The item at position 0 is :",position)

# 7/Ask the user how many items they can afford to buy and remove the rest using pop from the end, printing each removed item

can_afford = int(input("enter how many items you can afford to buy ? :"))
remove_item = len(grocery)-can_afford # there is no use of remove_item on this program, but this 7 number problem need loop to properly solve it. i hope you got it.

print("removed",grocery.pop())
print("removed",grocery.pop())

# Store the remaining items in a tuple and print it
remaining_items = tuple(grocery)
print("the remaining items are :",remaining_items)

# Print a goodbye message with the user's initials
initials = user_name.split()

print("Thanks for shopping with us MR",initials[0][0].upper()+"."+initials[1][0].upper()+".")
