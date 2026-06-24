n = int(input())
m = int(input())


print("*"*m)
for i in range(n-2):
    print("*"+" "*(m-2)+"*")
print("*"*m)