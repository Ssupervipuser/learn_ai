class HeroFighter(object):
    def __init__(self, power_int):
        if power_int > 100:
            self.power_int = 99
        else:
            self.power_int = power_int
    def power(self):
        return self.power_int

class AdvHeroFighter(HeroFighter):
    def __init__(self, power_int):
        if power_int > 100:
            self.power_int = power_int * 2
        else:
            self.power_int = 100

    def power(self):
        return self.power_int

class EnemyFighter(object):
    def attack(self):
        return 130


enemy = EnemyFighter()

# 1.
hero1 = HeroFighter(power_int=60)
if hero1.power() > enemy.attack():
    print('赢了')
elif hero1.power() == enemy.attack():
    print('平局')
else:
    print('输了')

# 2.
hero2 = HeroFighter(power_int=90)
if hero1.power() > enemy.attack():
    print('赢了')
elif hero1.power() == enemy.attack():
    print('平局')
else:
    print('输了')


# 3.
hero2 = HeroFighter(power_int=100)
if hero1.power() > enemy.attack():
    print('赢了')
elif hero1.power() == enemy.attack():
    print('平局')
else:
    print('输了')


# 4.
hero2 = AdvHeroFighter(power_int=100)
if hero1.power() > enemy.attack():
    print('赢了')
elif hero1.power() == enemy.attack():
    print('平局')
else:
    print('输了')