
class Player:
    def __init__(self, name, life):
        self.name = name
        self.Life = int(life)
    def drink_check_die(self):
        self.Life -= 1
        #출력
        if self.Life <= 0:
            return True
        else:
            return False
