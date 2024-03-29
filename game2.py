import random

apartment_asciiart = '''
    _       ____       _       ____      _____   __  __  U _____ u _   _     _____         ____      _      __  __  U _____ u 
U  /"\  u U|  _"\ uU  /"\  uU |  _"\ u  |_ " _|U|' \/ '|u\| ___"|/| \ |"|   |_ " _|     U /"___|uU  /"\  uU|' \/ '|u\| ___"|/ 
 \/ _ \/  \| |_) |/ \/ _ \/  \| |_) |/    | |  \| |\/| |/ |  _|" <|  \| |>    | |       \| |  _ / \/ _ \/ \| |\/| |/ |  _|"   
 / ___ \   |  __/   / ___ \   |  _ <     /| |\  | |  | |  | |___ U| |\  |u   /| |\       | |_| |  / ___ \  | |  | |  | |___   
/_/   \_\  |_|     /_/   \_\  |_| \_\   u |_|U  |_|  |_|  |_____| |_| \_|   u |_|U        \____| /_/   \_\ |_|  |_|  |_____|  
 \\    >>  ||>>_    \\    >>  //   \\_  _// \\_<<,-,,-.   <<   >> ||   \\,-._// \\_       _)(|_   \\    >><<,-,,-.   <<   >>  
(__)  (__)(__)__)  (__)  (__)(__)  (__)(__) (__)(./  \.) (__) (__)(_")  (_/(__) (__)     (__)__) (__)  (__)(./  \.) (__) (__) 
    '''

def game2(players,start_idx):
    
    print("=================================================================================================================================")
    print(apartment_asciiart)
    print("🏢🏢🏢 아~파트 아파트 아~파트 아파트 🏢🏢🏢")
    print("=================================================================================================================================")
    leader = players[start_idx].name
    number = 0
    print(f"술래는 {leader}!")
    if (start_idx == 0):
        number = int(input(f"몇 층?! 5층부터 30층 사이에서 고르시오 : "))
    else:
        number = random.randint(5, 30)
        print(f"몇 층?! : {number}")

    hands = [f"{player.name}" for player in players for _ in range(2)]

    random.shuffle(hands)

    for i in range(1, number + 1):
        current_hand = hands[(i - 1) % len(hands)]
        print(f"{i}층: {current_hand}")
        if i == number:
            loser = current_hand
            loser_index = 0
            for player in players:
                if (loser == player.name):
                    return loser_index
                else:
                    loser_index += 1
