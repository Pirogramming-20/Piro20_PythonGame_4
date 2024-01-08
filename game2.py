import random

def play_apartment_game(players):
    leader = random.choice(players)
    print(f"술래: {leader}")

    hands = [f"{player}의 손" for player in players for _ in range(2)]

    random.shuffle(hands)

    number = random.randint(10, 99)
    print(f"술래가 부른 숫자: {number}")

    for i in range(1, number + 1):
        current_hand = hands[(i - 1) % len(hands)]
        print(f"{i}층: {current_hand}")
        if i == number:
            loser = current_hand.split('의')[0]
            loser_index = players.index(loser)
            return loser_index