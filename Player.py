
class Player:
    def __init__(self, name, life):
        self.name = name
        self.life = int(life)
    def drink_check_die(self):
        print(self.name,"마셔")
        self.life -= 1
        #출력
        if self.life <= 0:
            return True
        else:
            return False
