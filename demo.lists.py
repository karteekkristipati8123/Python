# Creating list with numbers
List1 =[10,20,30,40,50]
print("\n Numbers in list:")
print(List1)

# Creating list with strings
List2 = ["Kristipati","Karteek","Reddy"]
print("\n Strings in list:")
# Accessing elements in list using index number
print(List2[0])
print(List2[2])

# Multi-deimensional list
List3 = [["Kristpati","Karteek"],["Reddy"]]
print(List3[0][1])
print(List3[1][0])

# Negitive indexing
List4 = [4,'karthik', 1,'Vikram',5 ,'London',9]
print(List4[-1])
print(List4[-4])

# Getting the size of the list
print(len(List4))
print(len(List3))

# addition elements desired position using insert() method
List5 = [1 ,2, 3, 4, 5]
print("initial list")
print(List5)

List5.insert(3,10)
List5.insert(5,50)

print("\n After insert:")
print(List5)

# reversing list
Mylist = [6,5,4,3,2,1]
Mylist.reverse()
print(Mylist)

# removing elements in list 
List6 = [1,2,3,4,5]
print("Before remove")
print(List6)
List6.remove(2)
List6.remove(4)
print("\n After remove")
print(List6)