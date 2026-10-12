"""
print("Create a dynamic list of your friends")
friends=[]
friends.append("Ramesh")
friends.append("Ramya")
friends.append("Abdul")
print(friends)
print("length of list ",len(friends))
friends.append(4)
print(friends)
print("create a dynamics list of your favourite food")
foodlist=[]
totalnum=int(input("Enter the number of food which you like"))
for num in range(totalnum):
    food = input("Enter the food which you like")
    foodlist.append(food)
print("my favourite food ",foodlist)
"""
print("dynamic dictionary of aadhars number of your family members")
total=int(input("Enter total number of people in your family"))
aadhardict={}
for num  in range(total):
    name=input("Enter name")
    aadhar = input("Enter aadhar number")
    aadhardict[aadhar]=name
print("details of my family aadhar numbers",aadhardict)
               


