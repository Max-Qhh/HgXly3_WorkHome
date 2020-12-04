# -*- coding: utf-8 -*-
'''
1、自己写一个面向对象的例子：
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=短毛，
添加一个新的方法， 会捉老鼠，
复写父类的‘【会叫】的方法，改成【喵喵叫】
创建子类【狗】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=长毛，
添加一个新的方法， 会看家，
复写父类的【会叫】的方法，改成【汪汪叫】
调用name== ‘main’：
创建一个猫猫实例
调用捉老鼠的方法
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
调用【会看家】的方法
打印【狗狗的姓名，颜色，年龄，性别，毛发】。
2、将数据配置到yaml文件里
'''
import yaml


class Animal():
    # 属性：名称，颜色，年龄，性别
    name: str = "zoo"
    color: str = "毛色"
    age: int = 0
    gender: str = "性别"

    def __init__(self, name, color, age, gender):
        self.name = name  # 构造函数，初始化实例变量
        self.color = color
        self.age = age
        self.gender = gender

    # 类方法（会叫，会跑）
    def shout(self):
        print(f'{self.name} can shout')

    def run(self):
        print(f'{self.name} can run')


class cat(Animal):
    hair: str = "短毛"

    def __init__(self, hair, name, corol, age, gender):
        self.hair = hair
        super().__init__(name, corol, age, gender)

    def skill(self):
        print(f"{self.name} can catch mouse")

    def shout(self):
        print(f"{self.name}会喵喵叫")

    def get_cat(self):
        print(f"这是{self.name},毛色是{self.color}的,年龄是{self.age}岁，"
              f"性别是{self.gender},{self.hair}")


'''
创建子类【狗】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=长毛，
添加一个新的方法， 会看家，
复写父类的【会叫】的方法，改成【汪汪叫】
'''


class dog(Animal):
    hari: str = "长毛"

    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        super().__init__(name, color, age, gender)

    def skill(self):
        print(f"{self.name}会看家")

    def shout(self):
        print(f"{self.name}会汪汪叫")


'''
调用name== ‘main’：
创建一个猫猫实例
调用捉老鼠的方法
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
调用【会看家】的方法
打印【狗狗的姓名，颜色，年龄，性别，毛发】。
调用yaml
'''

if __name__ == '__main__':
    print("yaml调用")
    with open("animals.yml", encoding="UTF-8") as f:
        animals = yaml.safe_load(f)
        print("这是一个在yaml调用的一只小猫咪：")
        print(animals["cat1"])
        print("名字叫：", animals["cat1"]["name"])
        cat1_color = animals["cat1"]["color"]
        print(f"tom是{cat1_color}的~\n")
        print("这是一个在yaml调用的一只小狗子：")
        print(animals["dog1"])

    print("\n这是实例变量，DaDaDa~~~~Da~~~Da~——————:")
    cat1 = cat('短毛', 'tom', 'blue and white', 2, '小公猫')
    cat1.get_cat()
    cat1.skill()
    cat1.shout()
