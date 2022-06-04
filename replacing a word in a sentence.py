a=input("Enter the sentence:")
e=[]
e=a.split()
b=input("enter the word you want to change:")
c=input("enter the word you want to insert:")
z=""
for x in e:
    if x==b:
        z=z+c+" "
    else:
        z=z+x+" "
print(z)
mult
n=int(input("Enter the digit:"))
for i in range(1,11):
    print(n,"*",i,"=",(n*i))
