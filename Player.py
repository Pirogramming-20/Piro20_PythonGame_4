
class Player:
    def __init__(self, name, life):
        self.name = name
        self.life = int(life)
    def drink_check_die(self):
        self.life -= 1
        #출력
        print(f" ヘ（゜◇、゜）ノ  {self.name} 한잔해~   ヘ（゜◇、゜）ノ")
        if self.life <= 0:
            return True
        else:
            return False
