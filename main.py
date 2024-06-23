import random

def start_message():
  print('じゃんけんスタート')

def get_my_hand():
  print('自分の手を入力してください')
  my_hand = int(input('0:グー, 1:チョキ, 2:パー'))
  print('自分の手:', my_hand)
  return my_hand

def get_you_hand():
  you_hand = random.randint(0, 2)
  print('相手の手:', you_hand)
  return you_hand

def view_result():
  hand_diff = get_my_hand() - get_you_hand()
  if hand_diff == 0:
    print('あいこ')
  elif hand_diff == -1 or hand_diff == 2:
    print('勝ち')
  else:
    print('負け')

start_message()
view_result()
