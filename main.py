import random
from Player import Player

from game1 import game1
from game2 import game2
from game3 import game3
from game4 import game4
from game5 import game5

Game_start_Intro_Str = '''
______         _    _                     _____                         
| ___ \       | |  | |                   |  __ \                        
| |_/ / _   _ | |_ | |__    ___   _ __   | |  \/  __ _  _ __ ___    ___ 
|  __/ | | | || __|| '_ \  / _ \ | '_ \  | | __  / _` || '_ ` _ \  / _ 
| |    | |_| || |_ | | | || (_) || | | | | |_\ \| (_| || | | | | ||  __/
\_|     \__, | \__||_| |_| \___/ |_| |_|  \____/ \__,_||_| |_| |_| \___|
         __/ |                                                          
        |___/                                                           
'''
Game_Life_Select_Menu = ""

#게임 시작
def Game_start():
    print(Game_start_Intro_Str)
    while(True):
        try:
            start_flag = input("게임을 진행할까요? (y/n) :")
            if start_flag != 'y' and start_flag != 'n':
                raise Exception("y/n만 입력 가능")
        except Exception as e:
            print(e)
        else:
            if start_flag == 'y':
                Game_input()
            else:
                return

def Game_input():
    while(True):
        try:
            #사용자 인 풋 받기
            player_user_name = input("당신의 이름은? : ")
            #주량 선택하기
            player_user_life = int(input("당신의 주량은? : "))
            if player_user_life > 10 or player_user_life < 0:
                raise Exception("주량은 0~10까지의 정수")
            player_user = Player(player_user_name,player_user_life)
        except ValueError:
            print("주량은 0~10까지의 정수")
        except Exception as e:
            print(e)
        else:
            Game_setting_players(player_user)

player_name_list = ["은서","하연", "연서", "예진", "헌도"]

def Game_setting_players(player_user):
    players_list = []
    players_list.append(player_user)
    while(True):
        try:        
            num_add_player= int(input("추가 참가자 수 : "))
            if num_add_player > 5 or num_add_player <= 0:
                raise("추가 참가자 수는 0~5")
        except Exception as e:
            print(e)
        else:   
            #참가자 추가
            random.shuffle(player_name_list)
            for i in range(num_add_player):
                name_add = player_name_list.pop()
                player_Life = random.randint(5, 10)#주량
                players_list.append(Player(name_add,player_Life))
            for player in players_list:
                print(f"이름 : {player.name} 주량 : {player.life}")
            Game_SoulGame(players_list)

def Game_SoulGame(players_list):
    start_idx = random.randint(0,len(players_list)-1)
    while(True):
        game_number = int(input("게임 골라 :"))
        
        #미니 게임 진행!
        try:
            if game_number == 1:
                loser_idx = game1(players_list,start_idx)
            elif game_number == 2:
                loser_idx = game2(players_list,start_idx)
            elif game_number == 3:
                loser_idx = game3(players_list,start_idx)
            elif game_number == 4:
                loser_idx = game4(players_list,start_idx)
            elif game_number == 5:
                loser_idx = game5(players_list,start_idx)
            else:
                raise("1~5까지만 입력해주세요")
        except Exception as e:
            print(e)

        #진 사람 처리!
        if(players_list[loser_idx].drink_check_die()):
            print(players_list[loser_idx].name, "사망")
            break

        start_idx = loser_idx 

Game_start()