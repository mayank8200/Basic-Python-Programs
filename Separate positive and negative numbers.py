#Write a program to filter positive nos from a list

b=int(input("Enter the number of elements:"))
a=[]
for i in range(b):
    i=int(input("Enter the number:"))
    a.append(i)
neg=[]
pos=[]
for i in a:
    if(i<0):
        neg.append(i)
    else:
        pos.append(i)
print(pos,neg)
