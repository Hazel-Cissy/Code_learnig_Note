
#这是一个计算机编写的开发成雪
#1.首先 我们需要定义一个用户的交互界面

Way_Math ={1:"加法",2:"减法",3:"乘法",4:"除法"}

print("welcome the MATH,Pleace choise your Way")
while True:
    print("1.加法\n2.减法\n3.乘法\n4.除法")
    uers_Way_Choise = int(input("请输入你想要选择的计算方法："))


    if uers_Way_Choise in Way_Math:
        print("你的选择是:{},请输入运算数字".format(Way_Math[uers_Way_Choise]))
        num1 = float(input("第一个数："))
        num2 = float(input("第二个数："))
        if uers_Way_Choise == 1:
            print(num1 + num2)
        elif  uers_Way_Choise == 2:
            print(num1 - num2)
        elif uers_Way_Choise == 3:
            print(num1 * num2)
        elif uers_Way_Choise == 4:
            print(num1 / num2)
            if num2 == 0:
                print("错误：不能除以0")
            else:print(f"结果{num1/num2}")

    else:
        print("无效输入，请重新输入")

    another = input("是否继续计算？（yes/no）：").lower()#lower（）将大写字母返回小写字母
    if another != 'yes':
        print("感谢使用计算器，程序结束！")
        break

