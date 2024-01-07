import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
#get 요청시 우리 정보
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
hdr = {'User-Agent': user_agent}

Game_intro_str = (
    "이이잉 레코드"
    "주의 \033[1;31m이 게임은 파이썬 requests, BeautifulSoup selenium깔려있어야 진행이 가능합니다\033[0m"
)

def game3():
    print(Game_intro_str)
    theme_game = "" 
    while(1):
        try:
            mod = input("난이도를 고르세요 (1-쉬움,2-보통 ,3-어려움): ")
            # if mod != 1 and mod != 2 and mod != 3:
            #     raise Exception("잘못 입력하셨습니다")
            theme_game = input("가수나 그룹 이름을 적어주세요 :")
            url = f"https://www.melon.com/search/song/index.htm?q={theme_game}&section=artist&section=&searchGnbYn=Y&kkoSpl=N&kkoDp"
            response = requests.get(url, headers=hdr)
            if(response.status_code == 404 or response.status_code == 500):
                raise Exception("주소 오류")
            soup = bs(response.text, "html.parser")
            num_song_HTML = soup.select_one("#conts > div.section_song > h3 > strong > em")
            if num_song_HTML:
                num_songs = int(num_song_HTML.get_text())
                print(num_songs,"개의 곡 정보 존재")
                if(num_songs == 0):
                    raise Exception("그런 사람 몰라요~")    
                flag_game = input("취소하려면 n입력 계속 진행하려면 n이외의 아무키나 눌러주세여")
                if(flag_game == 'n'):
                    raise Exception("게임 재시작")
            else:
                raise Exception("그런 사람 몰라요~")
        except Exception as e:
            print(e)
        else:
            break
    #멜론에서 곡 가져오기 
    list_urls = []
    #request로 할랬는데 멜론이 자바스크립트로 페이지를 바꿔서 아무리 해도 안돼
    #페이지마다 일부 html fetch
    #50단위로 페이지 변화
    for i in range(1,num_songs,50):
        list_urls.append(f"https://www.melon.com/search/song/index.htm?startIndex={i}&pageSize=50&q={theme_game}&sort=hit&section=all&sectionId=&genreDir=")
    list_soups_for_songs = []
    #url들에 접속해 source get
    for url_i in list_urls:
        response = requests.get(url_i, headers=hdr)
        list_soups_for_songs.append(bs(response, "html.parser"))
    #집합에 저장
    
    set_song_ForGame = set() #중복 처리를 위한 집합
    for soup_i in list_soups_for_songs:
        songs = soup_i.select(".fc_gray")
        for song in songs:
            song = song.get_text()
            set_song_ForGame.add(song)

    songs_ForGame = list(set_song_ForGame) 
    print(songs_ForGame)
    # while(True):
    #     for player in players_list:
    #         if player.name == True:
    #             answer = input("노래 제목 입력")
    #         else:
    #             p_computer = random.randint(0, mod*5)
    #             if p_computer == 0:
    #                 print("내 패배다.......")
    #             else :
    #                 answer = songs_ForGame.pop(0)
    #         if answer in songs_ForGame:
    #             print("정답 인정")
    #         else:
    #             print(player.name,"마셔라")
    #             return player
game3()