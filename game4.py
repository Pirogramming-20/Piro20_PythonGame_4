import random
#  DOWN DOWN DOWN!! 𖦹ࡇ𖦹 𖦹ࡇ𖦹 𖦹ࡇ𖦹

def game4(players, start_index, name):
    current_player = players[start_index]  # 시작 플레이어
    rejection_count = 0
    print("술도 마셨는데 좋아 게임할까~ ")

    while True:
        if current_player == name:  # '나'일 때
            print("누가 좋아?:")
            for i, p in enumerate(players[1:], 1): #'나' 0번째 인덱스
                print(f"{i}: {p.name}")
            
            try:
                choice= int(input())

                if choice in i:
                    select_player = players[choice]
                    print(f"{current_player.name} : {select_player.name} 좋아~")

                #범위 내 숫자 아닐땐 예외처리
                else:
                    print("제대로 입력하세요")
            except ValueError:
                    print("숫자를 입력하세요.")
          
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
                print(f" ヘ（゜◇、゜）ノ  {select_player.name} 한잔해~   ヘ（゜◇、゜）ノ")
                loser_index = players.index(select_player)
                return loser_index
                break


