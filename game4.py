import random

# #{select_player.name} DOWN DOWN DOWN!! 𖦹ࡇ𖦹 𖦹ࡇ𖦹 𖦹ࡇ𖦹
# class Player:
#     def __init__(self, name, limit):
#         self.name = name
#         self.limit = limit
#         self.drinks_had = 0

#     def drink(self):
#         self.drinks_had += 1
#         if self.drinks_had > self.limit:
#             return True
#         return False


def game4(players, start_index, name):
    current_player = players[start_index]  # 시작 플레이어
    rejection_count = 0

    while True:
        if current_player == name:  # '나'일 때
            print("다음 지목할 사람을 선택하세요:")
            for i, p in enumerate(players[1:], 1):
                print(f"{i}: {p.name}")
            choice = int(input()) - 1
            #숫자 아닐땐 예외처리
            select_player = players[choice + 1]
            print(f"{current_player.name} : {select_player.name} 좋아~")
        else:
            select_player = random.choice([p for p in players if p != current_player])
            print(f"{current_player.name} : {select_player.name} 좋아~")

        reaction = random.choice(["나도 좋아❤️", "칵~퉤🤮"])
        print(f"{select_player.name}: {reaction}")

        if reaction == "나도 좋아❤️":
            current_player = select_player
            rejection_count = 0
        else:
            rejection_count += 1
            if rejection_count == 3:
                print(f" ヘ（゜◇、゜）ノ  누가 술을 마셔 {select_player.name}가 술을 마셔.  {select_player.name} 한잔해~   ヘ（゜◇、゜）ノ")
                break

 
       

    return #패자의 인덱스.

# 플레이어 객체 생성
#player_a = Player("a", 3) # 입력 값,  나머진 랜덤으로 받아오기
#player_b = Player("b", 5)
#player_c = Player("c", 2)
#player_d = Player("d", 4)

# 플레이어 객체들을 포함하는 리스트 생성
#players = [player_a, player_b, player_c, player_d]

# 게임 시작과 결과 
#game_result = game4(players)
#print("\n".join(game_result))


