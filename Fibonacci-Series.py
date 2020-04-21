print("Febonacci Series")
n=int(input("Enter the number of elements from the series :"))
print("you have entered ",n)
#code
a=0
b=1
next=0
i=1
if n>0:
    print(0)
if n>1:
    print(1)
if n>2:
    while i<=n-2:
        next=a+b;
        print(next)
        a=b
        b=next
        i+=1
if n<=0:
    print("minimun number required is 1")
