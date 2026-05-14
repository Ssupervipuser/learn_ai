class HeroFighter(object):
    def power(self):
        return 60

class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80

class EnemyFighter(object):
    def attack(self):
        return 70

# todo 多态发生的地方：每次调用object_play函数因为传参不同、导致结果不同
def object_play(hero: HeroFighter, enemy: EnemyFighter):
    # hero.power() 同一个函数，不同对象，结果不同
    if hero.power() > enemy.attack():
        print('我方胜利')
    elif hero.power() == enemy.attack():
        print('不相上下')
    else:
        print('我方失利')

hero1 = HeroFighter()
hero2 = AdvHeroFighter()
enemy = EnemyFighter()

# 第一次战斗 1代飞机vs敌机
object_play(hero1, enemy)
# 第2次战斗 2代飞机vs敌机
object_play(hero2, enemy)


