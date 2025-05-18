import keyboard
import time
import random
import os

QUESTION_NUM = 2                                                   # 文章を入力する回数
input_data_all = []                                                 # 入力された全てのデータ
input_data = []                                                     # 入力されたデータ
chose_merosu_file = ''                                              # 選択されたローマ字タイプのメロス
rome_type = ''                                                      # 選択されたローマ字タイプ
text = []                                                           # 入力するテキスト(漢字、ひらがな、ローマ字の順)
text_lst = []                                                       # 実際に使用したテキスト群
save_file_timestamp = str(time.time())                              # 保存するファイルに使用するタイムスタンプ
save_file = './datas/input_' + save_file_timestamp + '.csv'         # 入力情報を保存
save_file_all = './datas/all_' + save_file_timestamp + '.csv'       # すべての入力情報を保存
save_file_text = './datas/text_' + save_file_timestamp + '.csv'     # 使用したテキストを保存する

# 入力指示を表示する関数
def display_guide(QUESTION_NUM, question_cnt, text_cnt, text_num):
  os.system('cls')
  print(f"[{ question_cnt }/{ QUESTION_NUM }] 表示された文字を入力してください。")
  print(f"　入力　： { text[text_num]['kanji'] }")
  print(f"　かな　： { text[text_num]['kana'] }")
  print(f"ローマ字： { text[text_num]['rome'] }")
  print("　　　　　 " + ( "-" * text_cnt ))

# まず、ローマ字タイプを選択する
print("ローマ字タイプを選択してください")
while True:
  rome_type = input("a or b: ")
  if rome_type == 'a':
    chose_merosu_file = 'merosu_short_rome_a.csv'
    break
  elif rome_type == 'b':
    chose_merosu_file = 'merosu_short_rome_b.csv'
    break
  else:
    print("aかbを入力してください")
    
# メロスデータを読み込み
with open('merosu_short.csv', mode='r', encoding='utf-8') as f:
  with open('merosu_short_kana.csv', mode='r', encoding='utf-8') as kf:
    with open(chose_merosu_file, mode='r', encoding='utf-8') as rf:
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
display_guide(QUESTION_NUM, question_cnt, text_cnt, text_num)
text_lst.append(text[text_num]['kanji'])
while True:
  input_key = keyboard.read_key()
  input_data_all.append({'key':input_key, 'timestamp':time.time()})
  if input_key != "":
    # 途中脱出
    if input_key == 'esc':
      break

    # 正しい入力だった場合、結果を保存
    if input_key == text[text_num]['rome'][text_cnt]:
      text_cnt += 1
      display_guide(QUESTION_NUM, question_cnt, text_cnt, text_num)
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
          input_data.append({'key': 'change', 'timestamp':time.time()})  # 文章が変わるタイミング
          display_guide(QUESTION_NUM, question_cnt, text_cnt, text_num)
          text_lst.append(text[text_num]['kanji'])

# 使用したテキスト群を保存
with open(save_file_text, mode='w', encoding='utf-8') as f:
  for text in text_lst:
    f.write(text + "\n")

# 入力した全てのキー情報を保存
with open(save_file_all, mode='w', encoding='utf-8') as f:
  for i in range(len(input_data_all)):
    f.write(f"{input_data_all[i]['key']},{input_data_all[i]['timestamp']}\n")

# 結果を保存
before_timestamp = 0.0
text = ""
with open(save_file, mode='w', encoding='utf-8') as f:
  for i, data in enumerate(input_data):
    # コンソールに表示
    current_key = data['key']
    timestamp = data['timestamp']
    # print(f"{current_key}, {timestamp-before_timestamp}")
    before_timestamp = timestamp
    text += current_key

    # ファイルに保存
    f.write(f"{current_key},{timestamp}\n")

os.system('cls')
print("ご協力ありがとうございました！")