import keyboard
import time
import random
import os

QUESTION_NUM = 3   # 文章を入力する回数
input_data = []     # 入力されたデータ
text = []           # 入力するテキスト(漢字、ひらがな、ローマ字の順)

# 入力指示を表示する関数
def display_guide(QUESTION_NUM, question_cnt, text_cnt, text_num ):
  os.system('cls')
  print(f"[{ question_cnt }/{ QUESTION_NUM }] 表示された文字を入力してください。")
  print(f"　入力　： { text[text_num]['kanji'] }")
  print(f"　かな　： { text[text_num]['kana'] }")
  print(f"ローマ字： { text[text_num]['rome'] }")
  print("　　　　　 " + ( "-" * text_cnt ))

# メロスデータを読み込み
with open('merosu_short.csv', mode='r', encoding='utf-8') as f:
  with open('merosu_short_kana.csv', mode='r', encoding='utf-8') as kf:
    with open('merosu_short_rome.csv', mode='r', encoding='utf-8') as rf:
      while True:
        kanji = f.readline()
        kana = kf.readline()
        rome = rf.readline()
        if kanji == '':
          break
        text.append({
          'kanji': kanji.replace('\n', ''),
          'kana': kana.replace('\n', ''),
          'rome': rome.replace('\n', '').replace(' ', '')
        })

# 入力処理
question_cnt = 1                        # 現在の問題番号
text_cnt = 0                            # 入力文字数
text_num = random.randint(0, len(text)) # 入力する文章(とりあえずランダム)
display_guide(QUESTION_NUM, question_cnt, text_cnt, text_num )
while True:
  input_key = keyboard.read_key()
  if input_key != "":
    # 途中脱出
    if input_key == 'esc':
      break

    # 正しい入力だった場合、結果を保存
    if input_key == text[text_num]['rome'][text_cnt]:
      text_cnt += 1
      display_guide(QUESTION_NUM, question_cnt, text_cnt, text_num )
      input_data.append({'key':input_key, 'timestamp':time.time()})
      
      if text_cnt >= len(text[text_num]['rome']):
        if question_cnt == QUESTION_NUM:
          # 事前に登録された回数の文章を入力し終わった場合、ループを抜けて結果を表示する
          break
        else:
          # 事前に登録された回数の文章を入力し終わっていな場合、新しい文章を表示する
          question_cnt += 1
          text_cnt = 0
          text_num = random.randint(0, len(text))
          display_guide(QUESTION_NUM, question_cnt, text_cnt, text_num )

# 結果を表示
print("----------")
print("結果")
before_timestamp = 0.0
text = ""
for i, data in enumerate(input_data):
  current_key = data['key']
  timestamp = data['timestamp']
  print(f"{current_key}, {timestamp-before_timestamp}")
  before_timestamp = timestamp
  # if i % 2 == 0:
  text += current_key

print("----------")
print("入力された文字")
print(text)