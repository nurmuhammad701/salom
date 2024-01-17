a=input(">>> ")
b=10**len(a)
for i in a:
    b/=10
    i=int(i)
    b=int(b)
    print(f"{i*b}+",end="")
print("\b",end="")