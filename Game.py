# 导入第三方类
import random
import time


# 定义一个游戏类
class Game:
    # 初始化属性(后期都改为直接定义私有属性) 这个方法类似于java中的构造函数
    def __init__(self, name, blood):
        self.name = name
        self.blood = blood

    # 捅人的方法
    def poke(self, enemy):  # 捅人的方法
        """
        :param self 本类对象（哪个对象调用self就是哪个对象）
        :param enemy:  敌人
        :return:
        """
        enemy.blood -= 10
        info = "{}捅了{}一刀".format(self.name, enemy.name)
        print_info(info)

    def chop(self, enemy):
        """
        :param self 本类对象（哪个对象调用self就是哪个对象)
        :param enemy:  敌人
        :return:
        """
        enemy.blood -= 10
        info = "{}砍了{}一刀".format(self.name, enemy.name)
        print(info)

    def add_drug(self):
        """
        :param self 本类对象（哪个对象调用self就是哪个对象)
        :return:
        """
        if self.blood != 100:  # 如果随机到吃药的方法 判断血量是否等于初始血量 如果不等于再吃药
            self.blood += 10
            info = "玩家{}吃了药".format(self.name)
            print_info(info)

    def __str__(self):
        return "玩家{}还剩余{}血量".format(self.name, self.blood)


def role_message(oneself, enemy):
    """
    打印玩家信息方法
    :param oneself:
    :param enemy:
    :return:
    """
    print(oneself)
    print(enemy)
    print("==========华丽的分割线==========")


def print_info(msg):
    print(msg)


def go(oneself, enemy):
    """
    执行的方法 传入两个玩家
    :param oneself:
    :param enemy:
    :return:
    """
    role = random.randint(1, 2)  # 随机玩家
    attack = random.randint(1, 3)  # 随机方法 (1. 捅人 2.砍人 3. 嗑药 )
    if role == 1:  # 如果选择的是第一个英雄
        # 判断随机的是哪个动作
        oneself.poke(enemy) if attack == 1 else (oneself.add_drug() if attack == 3 else oneself.chop(enemy))
        #  打印信息
        if oneself.blood <= 100 or enemy.blood <= 100:
            role_message(oneself, enemy)
    elif role == 2:  # 如果选择的是第二个英雄
        # 判断随机的是哪个动作
        enemy.poke(oneself) if attack == 1 else (enemy.chop(oneself) if attack == 2 else enemy.add_drug())
        #  打印信息
        if oneself.blood <= 100 or enemy.blood <= 100:
            role_message(oneself, enemy)


player_one = Game("西门吹雪", 100)  # 创建玩家一
player_tow = Game("叶孤城", 100)  # 创建玩家二

while True:  # 循环
    # 两个玩家其中有一个血量耗尽 游戏结束
    if player_one.blood == 0:
        print("玩家{}血量耗尽,游戏结束".format(player_one.name))
        break
    elif player_tow.blood == 0:
        print("玩家{}血量耗尽,游戏结束".format(player_tow.name))
        break
        # 休息1秒
    time.sleep(1)
    # 否则继续游戏
    go(player_one, player_tow)
