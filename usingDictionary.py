#Write a program to get the max and min values from a dictionary
a={}
b=int(input("Enter the number of items:"))
for i in range(b):
    k=int(input("Enter the key:"))
    v=int(input("Enter the value:"))
    a[k]=v
min=a[1]
max=a[1]
for i in a.values():
    if(i<min):
        min=i
    if(i>max):
        max=i
print(min,max)

    
