import random
from Player import Player

from game1 import game1
# from game2 import game2()
# from game3 import game3()
from game4 import game4

Game_start_Intro_Str = ""
Game_Life_Select_Menu = ""

#게임 시작
def Game_init():
    print(Game_start_Intro_Str)
    try:
        start_flag = input("게임을 진행할까요? (y/n) :")
        if start_flag != 'y' and start_flag != 'n':
            raise Exception("y/n만 입력 가능")
    except Exception as e:
        print(e)
    else:
        if start_flag == 'y':
            Game_SoulGame()
        else:
            return
        
#이름 받고 주량 선택
player_name_list = ["은서","하연", "연서", "예진", "헌도"]

def Game_SoulGame():
    #사용자 인 풋 받기
    real_player_name = input("당신의 이름은? : ")
    #주량 선택하기
    real_player_Life = input("당신의 주량은? : ")
    #플레이어 객체 리스트
    players_list = []
    players_list.append(Player(real_player_name,real_player_Life))
    num_player= int(input("추가 참가자 수 : "))
    #참가자 추가
    random.shuffle(player_name_list)
    for i in range(num_player):
        name_add = player_name_list.pop()
        player_Life = random.randint(0, 10)#주량
        players_list.append(Player(name_add,player_Life))
    
    # #각 참가자 이름과 주량 출력
    # for player in players_list:
    #     print(f"이름: {player.name}, 주량: {player.Life}")


    start_idx = random.randint(0,len(players_list)-1)

    while(True):
        game_number = int(input("게임 골라 :"))
        
        #미니 게임 진행!
        if game_number == 1:
            loser_idx = game1(players_list,start_idx,real_player_name)
        elif game_number == 2:
            loser_idx = game2(players_list,real_player_name,)
        elif game_number == 3:
            loser_idx = game3(players_list,real_player_name,start_idx)
        elif game_number == 4:
            loser_idx = game4(players_list,start_idx,real_player_name)
        
        #진 사람 처리!
        if(players_list[loser_idx].drink_check_die()):
            print(players_list[loser_idx].name, "사망")
            break
        start_idx = loser_idx 

Game_init()