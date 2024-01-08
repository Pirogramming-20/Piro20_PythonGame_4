import random

#play_apartment_game
def game2(players,start_idx):
    print("===============================아~파트 아파트 아~파트 아파트===============================")
    leader = players[start_idx].name
    number = 0
    if (start_idx == 0):
        number = int(input(f"몇 층?! 🫠 : "))
    else:
        number = random.randint(1, 20)
        print(f"몇 층?! 🫠 : {number}")

    hands = [f"{player.name}의 손" for player in players for _ in range(2)]

    random.shuffle(hands)

    for i in range(1, number + 1):
        current_hand = hands[(i - 1) % len(hands)]
        print(f"{i}층: {current_hand}")
        if i == number:
            loser = current_hand.split('의')[0]
            loser_index = 0
            for player in players:
                if (loser == player.name):
                    return loser_index
                else:
                    loser_index += 1