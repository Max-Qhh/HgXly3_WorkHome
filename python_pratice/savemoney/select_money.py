# # -*- coding: utf-8 -*-
# import send_money
# import money

# 工资查询模块 select_money，用来展示工资数额
from python_pratice.savemoney import send_money, money

sum = 0


# send_money=1000
def select_money():
    while 1:
        # print(type(send_money.send_money()))
        print(type(money.saved_money))
        n = input("请输入发工资次数:")
        try:
            n = eval(n)
            sum = n * send_money.send_money() + money.saved_money
            print(f"工资数额:{sum}", )
            break
        except SyntaxError:
            print("请输入整数后重新查询\n")
        except NameError:
            print("请输入整数后重新查询\n")
