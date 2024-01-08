import requests
from bs4 import BeautifulSoup as bs
import random

#get 요청시 우리 정보
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
hdr = {'User-Agent': user_agent}

Game_intro_str = (
    "이이잉 레코드"
    "\033[1;31m주의! 이 게임은 파이썬 requests, BeautifulSoup이 깔려있어야 진행이 가능합니다\033[0m"
)
def game3_setting():
    theme_game = "" 
    #게임 시작 정보 설정
    while(1):
        try:
            mod = int(input("난이도를 고르세요 (1-쉬움,2-보통 ,3-어려움): "))
            if mod != 1 and mod != 2 and mod != 3:
                raise Exception("잘못 입력하셨습니다")
            theme_game = input("가수나 그룹 이름을 적어주세요 : ")
            url = f"https://www.melon.com/search/song/index.htm?q={theme_game}&section=artist&section=&searchGnbYn=Y&kkoSpl=N&kkoDp"
            response = requests.get(url, headers=hdr)
            #주소가 이상하거나 멜론 홈페이지가 이상할 때
            if(response.status_code == 404 or response.status_code == 500):
                raise Exception("주소 오류")
            #문제 없으므로 bs객체로
            soup = bs(response.text, "html.parser")
            # 노래 개수를 가지는 bs객체 select
            num_song_HTML = soup.select_one("#conts > div.section_song > h3 > strong > em")
            if num_song_HTML:
                num_songs = int(num_song_HTML.get_text())
                print(num_songs,"개의 곡 정보 존재")
                if(num_songs == 0):
                    raise Exception("그런 사람 몰라요~")    
                flag_game = input("취소하려면 n 계속 진행하려면 n이외의 아무키나 눌러주세여")
                if(flag_game == 'n'):
                    raise Exception("게임 재시작")
            # 노래 개수를 받지 못했을때
            else:
                raise Exception("그런 사람 몰라요~")
        except ValueError:
            print("이건 멜론이 잘못했어")
        except Exception as e:
            print(e)
        else:
            return theme_game, num_songs, mod
    
def game3_get_songs(theme_game, num_songs):
    #멜론에서 곡 가져오기 
    list_urls = []
    #request로 할랬는데 멜론이 자바스크립트로 페이지를 바꿔서 아무리 해도 안돼 => 페이지 바꿀 때 마다 추가적인 html 받음
    #페이지마다 일부 html fetch
    #50단위로 페이지 변화
    for i in range(1,num_songs,50):
        list_urls.append(f"https://www.melon.com/search/song/index.htm?startIndex={i}&pageSize=50&q={theme_game}&sort=hit&section=all&sectionId=&genreDir=")
    list_soups_for_songs = []
    #url들에 접속해 source get
    for url_i in list_urls:
        response = requests.get(url_i, headers=hdr)
        list_soups_for_songs.append(bs(response.text, "html.parser"))#50개씩 저장된 페이지
    #리스트에 저장
    list_songs_ForGame = []
    #페이지 마다 받은 정보 리스트에 추가
    for soup_i in list_soups_for_songs:
        songs = soup_i.select(".fc_gray")
        for song in songs:
            song = song.get_text()
            list_songs_ForGame.append(song)
    return list_songs_ForGame
    
def game_setting_songs(list_songs_ForGame):
    extra_answer = []
    for song in list_songs_ForGame:
        #띄어쓰기는 봐주자
        if ' ' in song:
            song_NoWhitespace = song.replace(' ', '')    
            extra_answer.append(song_NoWhitespace)    
        #()부분 제외
            if '(' in song:
                extra_answer.append(song.split('(')[0].strip())
                extra_answer.append(song_NoWhitespace.split('(')[0])
                #영어 이름(맨뒤에 .이 아니면)
                if song.split('(')[1].strip(')')[-1] != '.':
                    extra_answer.append(song.split('(')[1].strip(')'))
                    extra_answer.append(song_NoWhitespace.split('(')[0].strip(')'))
    list_songs_ForGame += extra_answer
    
    num_answer = len(list_songs_ForGame)
    print("띄어쓰기와 영어이름를 감안해서",num_answer,"개의 제목이 있어요!")
    print(list_songs_ForGame)
    return list_songs_ForGame

def game3_ordering_players(players_list, start_idx):
    # 순서 정하기
    players_list_ordered = []
    #start_idx를 제외한 플레이어는 추가 후 리스트 셔플 
    for i in range(len(players_list)):
        if i != start_idx:
            players_list_ordered.append(players_list[i])
    random.shuffle(players_list_ordered)
    #start_idx인 플레이어 맨 앞에 삽입
    players_list_ordered.insert(0,players_list[start_idx])
    print("순서는")
    for player in players_list:
        print(player.name)
    return players_list_ordered
    
    
def game3(players_list,start_idx):
    #인트로 출력
    print(Game_intro_str)
    
    #게임 세팅
    theme_game, num_songs, mod = game3_setting()

    print("곡 정보를 가져오고 있습니다...........")
    list_songs_ForGame = game3_get_songs(theme_game, num_songs)
    #띄어쓰기와 영어이름를 감안
    list_songs_ForGame = game_setting_songs(list_songs_ForGame)
    
    players_list_ordered = game3_ordering_players(players_list, start_idx)

    #게임진행
    while(True):    
        for player in players_list_ordered:
            if player == players_list[0]:
                answer = input("노래 제목 입력 : ")
            else:
                p_computer = random.randint(0, mod * 5)
                if p_computer == 0:
                    print(f"{player.name}: 내 패배다.......")
                    return players_list.index(player)
                else :
                    answer = list_songs_ForGame[0]
            if answer in list_songs_ForGame:  
                print(f"{player.name}: {answer}정답!")
                list_songs_ForGame.remove(answer)
            else:
                print(f"{answer}는 {theme_game}의 곡이 아닙니다 당첨")
                return players_list.index(player)