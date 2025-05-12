import keyboard
import time
import random
import os

input_data = []     # 入力されたデータ
text = []           # 入力するテキスト(漢字、ひらがな、ローマ字の順)

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
i = 0                                   # 入力文字数
text_num = random.randint(0, len(text)) # 入力する文章(とりあえずランダム)
print(f"　入力　： { text[text_num]['kanji'] }")
print(f"　かな　： { text[text_num]['kana'] }")
print(f"ローマ字： { text[text_num]['rome'] }")
while True:
  input_key = keyboard.read_key()
  if input_key != "":
    # 途中脱出
    if input_key == 'esc':
      break

    # 正しい入力だった場合、結果を保存
    if input_key == text[text_num]['rome'][i]:
      i += 1
      os.system('cls')
      print(f"表示された文字を入力してください。")
      print(f"　入力　： { text[text_num]['kanji'] }")
      print(f"　かな　： { text[text_num]['kana'] }")
      print(f"ローマ字： { text[text_num]['rome'] }")
      print("　　　　　 " + ( "-" * i ))
      input_data.append({'key':input_key, 'timestamp':time.time()})
      
      if i >= len(text[text_num]['rome']):
        break

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