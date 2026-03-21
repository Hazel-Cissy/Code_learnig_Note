#非递归
while True:

    n = int(input())
    sum = 1
    for i in range(1,n+1):
        sum *= i
    print(sum)

    if n == "no":
        break