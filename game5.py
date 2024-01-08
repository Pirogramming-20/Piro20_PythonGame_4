import random

def communist(players):
    print("공 산당! 공산당 공 산당!")
    cur_pointer = random.choice(players)
    prev_pointer = None

    object = random.choice([x for x in players if x != cur_pointer])
    print(f"{cur_pointer}가 {object}에게 '동무'라고 말했습니다.")
    prev_pointer = cur_pointer
    cur_pointer = object

    while True:
        available = [x for x in players if x != cur_pointer and x != prev_pointer]
        object = random.choice(available)
        choose = random.choice(["동무", "마시라우"]) if len(available) > 1 else "동무"
        print(f"{cur_pointer}: {object}~ {choose}!")

        if choose == "마시라우":
            print(f"술을 마셔야 하는 사람은 {object}입니다.")
            return players.index(object)  # 패자의 인덱스 반환
        else:
            prev_pointer = cur_pointer
            cur_pointer = object