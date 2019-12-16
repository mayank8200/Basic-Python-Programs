#Write a program to get the max and min values from a dictionary
a={}
b=int(input("Enter the number of items:"))
for i in range(b):
    k=int(input("Enter the key:"))
    v=input("Enter the value:")
    a[k]=v
l=[]
for i in a.values():
    l.append(i)
print("The max is",max(l))    
print("The min is",min(l))
