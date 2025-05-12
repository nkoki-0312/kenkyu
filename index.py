import keyboard
import time

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

print("文字を入力してください")

# 値取得
i = 0
while True:
  input_key = keyboard.read_key()
  if input_key != "":
    if input_key == 'esc':
      break
    input_data.append({'key':input_key, 'timestamp':time.time()})
    print(f"{i}: {input_data[i]}")
    i += 1

print("----------")
print("結果")
before_timestamp = 0.0
text = ""
for i, data in enumerate(input_data):
  current_key = data['key']
  timestamp = data['timestamp']
  print(f"{current_key}, {timestamp-before_timestamp}")
  before_timestamp = timestamp
  if i % 2 == 0:
    text += current_key

print("----------")
print("入力された文字")
print(text)