n = int(input("Enter you n : "))
m = n
# print(n,type(n))
# i=1
tmp = 1
while (n>1):
    tmp*=n
    n-=1
    # print("n=",n)
    if (n==1):
        break
print(m,"! =",tmp)