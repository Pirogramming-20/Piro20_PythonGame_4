import random

def game4(players, start_index):
    name = players[0]
    current_player = players[start_index]  # 시작 플레이어
    rejection_count = 0
    print('''
        _                                               
        (_)                                              
         _   ___    __ _    __ _   __ _  _ __ ___    ___ 
        | | / _ \  / _` |  / _` | / _` || '_ ` _ \  / _  
        | || (_) || (_| | | (_| || (_| || | | | | ||  __/
        | | \___/  \__,_|  \__, | \__,_||_| |_| |_| \___|
       _/ |                 __/ |                        
      |__/                 |___/                         
        ''')
    print("======================================술도 마셨는데 좋아 게임할까~===================================")

    while True:
        if current_player == name:  # '나'일 때
            print("❓ 누가 좋아 ❓")
            for i, p in enumerate(players[1:], 1): #'나' 0번째 인덱스
                print(f"{i}: {p.name}", end="  ")
            
            try:
                choice= int(input())

                if choice in range(1, len(players)):
                    select_player = players[choice]
                    print(f"{current_player.name} : {select_player.name} 좋아~")

                #범위 내 숫자 아닐땐 예외처리
                else:
                    print(f"1 ~ {len(players)}중에 입력하세요")
            except ValueError:
                    print("숫자를 입력하세요.")
          
        else:
            select_player = random.choice([p for p in players if p != current_player])
            print(f"{current_player.name} : {select_player.name} 좋아~")
        
        if select_player == name:
            while(True):
                try: 
                    reaction_input = int(input("1 : 나도 좋아❤️  2 : 칵~퉤🤮 "))
                    if reaction_input != 1 and reaction_input != 2:
                        raise Exception("1과 2중에 선택해주세요")
                except ValueError:
                    print("숫자를 입력하세요.")
                except Exception as e:
                    print(e)
                else:
                    break
            reaction = "나도 좋아❤️" if reaction_input == 1 else "칵~퉤🤮"
        else:
            reaction = random.choice(["나도 좋아❤️", "칵~퉤🤮"])
        print(f"{select_player.name}: {reaction}")

        if reaction == "나도 좋아❤️":
            current_player = select_player
            rejection_count = 0
        else:
            rejection_count += 1
            if rejection_count == 3:
                loser_index = players.index(current_player)
                return loser_index


