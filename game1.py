from Player import Player

from random import randint
#the_game_of_death
def game1(members, start_index):
  print("신난다 아~싸! 재미난다! 더 게임 오브 데스!")
  player_name = members[0].name
  target = ''
  names = []
  targets = []

  for player in members:
      names.append(player.name)

  if members[start_index].name == player_name:
      while True:
          target = input("누구를 가리킬까요? : ")
          if target == player_name:
              print("자기 자신은 안돼요!")
          elif target not in names:
              print("그런 이름을 가진 사람은 없어요!")
          else:
              break

      for player in members:
          if player.name == player_name:
              targets.append(names.index(target))
              continue

          while True:
              target_index = randint(0, len(members) - 1)
              if members[target_index].name == player.name:
                  continue
              targets.append(target_index)
              break

      number = int(input("숫자는?! : "))

      next = targets[start_index]
      cnt = 1
      while cnt < number:
          print(f"{cnt}: {members[next].name}")
          cnt += 1
          next = targets[next]

      print(f"{members[next].name}(이)가 걸렸습니다!")
      return next

  else:
      while True:
          target = input("누구를 가리킬까요? : ")
          if target == player_name:
              print("자기 자신은 안돼요!")
          elif target not in names:
              print("그런 이름을 가진 사람은 없어요!")
          else:
              break

      for player in members:
          if player.name == player_name:
              targets.append(names.index(target))
              continue

          while True:
              target_index = randint(0, len(members) - 1)
              if members[target_index].name == player.name:
                  continue
              targets.append(target_index)
              break

      number = randint(0, len(members) - 1)
      print(f"{members[start_index].name}(이)가 고른 숫자는? : {number}")

      next = targets[start_index]
      cnt = 1
      while cnt < number:
          print(f"{cnt}: {members[next].name}")
          cnt += 1
          next = targets[next]

      print(f"{members[next].name}(이)가 걸렸습니다!")
      return next