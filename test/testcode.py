class Monster:
    def __init__(self,func):
        self.func = func 

class Attack:
    def bite(self):
        print("bite")

    def stqr(self):
        print("strike")

    def sfde(self):
        print("slash")

    def bdsqf(self):
        print("kick")

attacks = Attack()
monster = Monster(attacks.bite)
monster.func()

