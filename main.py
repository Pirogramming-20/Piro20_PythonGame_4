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


Game_Select_Menu = """
=====================================================================================================
            1. 더 게임 오브 데스
            2. 아파트
            3. 레코드 게임
            4. 좋아 게임
            5. 공산단 게임
=====================================================================================================

          """

#게임 시작
def Game_start():
    #게임 인트로 출력
    print(Game_start_Intro_Str)
    #시작 여부
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
                return
            # start_flag == 'n'인 경우
            else: 
                return

def Game_input():
    #사용자 정보 입력 받기
    while(True):
        try:
            #사용자 인 풋 받기
            player_user_name = input("😊 당신의 이름은? : ")
            #주량 선택하기
            player_user_life = int(input("🍺 당신의 주량은? : "))
            if player_user_life > 10 or player_user_life < 1:
                raise Exception("주량은 1~10까지의 정수")
            player_user = Player(player_user_name,player_user_life)
        except ValueError:
            print("주량은 1~10까지의 정수")
        except Exception as e:
            print(e)
        else:
            Game_setting_players(player_user)
            return

player_name_list = ["은서","하연", "연서", "예진", "헌도"]

def Game_setting_players(player_user):
    players_list = []
    players_list.append(player_user)
    while(True):
        try:        
            num_add_player= int(input("😎 추가 참가자 수 : "))
            if num_add_player > 5 or num_add_player <= 0:
                raise Exception("추가 참가자 수는 0~5")
        except ValueError:
            print("추가 참가자 수는 정수")
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
                print(f"{player.name} 주량 : {player.life} 잔🍺")
            Game_SoulGame(players_list)
            return
        
def Game_SoulGame(players_list):
    start_idx = random.randint(0,len(players_list)-1)
    while(True):
        # 컴퓨터가 진행할때 너무 빠르게 되는 거 방지
        input("너 괜찮아❓ (다음 게임을 진행하려면 아무키나 눌러 주세요) : ")
        try:
            #사람이면 
            if start_idx == 0:
                print(Game_Select_Menu)
                print(f"{players_list[start_idx].name}가 좋아하는 랜덤게임🎰 무슨 게임🎮 게임 스타트👏")
                game_number = int(input("무슨 게임 할까? (1~5선택): "))
            #컴퓨터면
            else:
                game_number = random.randint(1,5)
                print(f"{players_list[start_idx].name}가 좋아하는 랜덤게임🎰 무슨 게임🎮 게임 스타트👏") 
            #미니 게임 진행!
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
                raise Exception("게임🎮은 다섯개~게임🎰은 다섯개🖐️🖐️~(1~5만 입력해주세요)")
        except ValueError:
            print("정수를 입력해주세요")        
        except Exception as e:
            print(e)

        #진 사람 처리! if문은 죽으면 실행
        if(players_list[loser_idx].drink_check_die()):
            print(players_list[loser_idx].name, "💀 DOWN 💀")
            print(players_list[loser_idx].name, "💀 DOWN 💀")
            print(players_list[loser_idx].name, "💀 DOWN 💀")
            print('''   
                  
                                                                                                            
                    __ _   __ _  _ __ ___    ___    ___  __   __  ___  _ __ 
                    / _` | / _` || '_ ` _ \  / _ \  / _ \ \ \ / / / _ \| '__|
                    | (_| || (_| || | | | | ||  __/ | (_) | \ V / |  __/| |   
                    \__, | \__,_||_| |_| |_| \___|  \___/   \_/   \___||_|   
                    __/ |                                                   
                    |___/     
                 
                                               
                ''')
            return
        
        for player in players_list:
            print(f"{player.name} : 현재 치사량까지  {player.life}잔 남음 🍺")
        print("=====================================================================================================")
        
        start_idx = loser_idx 

Game_start()