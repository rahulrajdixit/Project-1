#Assigning elements to different lists
list1=[]
list2=[]
for i in range(0,4):
    ele=int(input("Enter the element:"))
    list1.append(ele)
print(list1)
list2=list1
print(list2)
print()

#Accessing elements from a tuple
tuple=(100,200,300,400)
for i in range(0,4):
    print("Element ",i," is:",tuple[i])
print()

#Deleting different dictionary elements
dict={1:"Blue",2:"Red",3:"Green"}
print("Before deleting:",dict)
del dict[1]
print("After deleting:",dict)
