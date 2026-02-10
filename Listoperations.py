#LIST in python
a=["apple","banana","Mango"]
print(a)
 
#last access items
a=["apple","banana","Mango"]
print(a[1])
print(a[0]) 
print(a[-1])

#Range of indexing
a=["apple","banana","Mango"]
print(a[0:2])

#Change list item
a=["apple","banana","Mango"]
a[1]="orange"
print(a)

#Add list items
a=["apple","banana","Mango"]
a.append("orange")
print(a)

#inser list items
a.insert(1,"Cherry")
print(a)

#Extend list
List1=["l1","l2","l3"]
List2=["l4","l5","l6"]
List1.extend(List2)
print(List1)

#Remove list items
List1.remove("l2")
print(List1)

#Remove specific items
List1.pop(2)
print(List1)

#Loop in list
for x in List1:
  print(x)
