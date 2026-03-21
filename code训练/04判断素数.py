print("退出请输入：‘no'")
while True:
    a = int(input())
    flag = False
    for i in range(2,a):
        if a % i == 0:
            flag = True
            break
    if flag == False:
        print("素数")
    else:
        print("和数")

    if a == "no":
        break

