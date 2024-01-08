import random

def game2(players,start_idx):
    apartment_asciiart = '''
                        _                        _   
  __ _ _ __   __ _ _ __| |_ _ __ ___   ___ _ __ | |_ 
 / _` | '_ \ / _` | '__| __| '_ ` _ \ / _ \ '_ \| __|
| (_| | |_) | (_| | |  | |_| | | | | |  __/ | | | |_ 
 \__,_| .__/ \__,_|_|   \__|_| |_| |_|\___|_| |_|\__|
      |_|                                            
    '''
    print("--------------------------------------------------------")
    print(apartment_asciiart)
    print("--------------------------------------------------------")
    print("🏢🏢🏢 아~파트 아파트 아~파트 아파트 🏢🏢🏢")
    print("--------------------------------------------------------")
    leader = players[start_idx].name
    number = 0
    print(f"술래는 {leader}!")
    if (start_idx == 0):
        number = input(f"몇 층?! : ")
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
