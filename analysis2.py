import os
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'MS Gothic'  # グラフに日本語も表示させる

DATA_PATH = "./save_datas"                        # データが保存されているディレクトリ
alphabet = "abcdefghijlkmnopqrstuvwxyz-"          # だたのアルファベット
all_datas = []                                    # allファイルのリスト
input_datas = []                                  # inputファイルのリスト
text_datas = []                                   # textファイルのリスト
pair_datas = []

# データ取得
data_num = int( len(os.listdir(DATA_PATH)) / 3 )  # データ数
for i in range(data_num):
  all_datas.append([])
  input_datas.append([])
  text_datas.append([])
  with open(DATA_PATH + "/" + "all_" + str(i) + ".csv", mode="r", encoding="UTF-8") as f:
    while True:
      row = f.readline()
      if row == '':
        break
      save_data = row.replace("\n", "").split(",")
      save_data = {'key': save_data[0], 'timestamp': save_data[1]}
      all_datas[i].append(save_data)
  with open(DATA_PATH + "/" + "input_" + str(i) + ".csv", mode="r", encoding="UTF-8") as f:
    while True:
      row = f.readline()
      if row == '':
        break
      save_data = row.replace("\n", "").split(",")
      save_data = {'key': save_data[0], 'timestamp': save_data[1]}
      input_datas[i].append(save_data)
  with open(DATA_PATH + "/" + "text_" + str(i) + ".csv", mode="r", encoding="UTF-8") as f:
    while True:
      row = f.readline()
      if row == '':
        break
      text_datas[i].append(row.replace("\n", ""))

# 前後の入力値ごとの平均時間
tmp = []   # 特定のアルファベットの組み合わせの入力にかかる時間を保存しておく
for n, datas in enumerate(input_datas):
  pair_datas.append([])
  for i in range(27):
    for j in range(27):
      tmp = []
      for k in range(len(datas)):
        if k != 0:
          if datas[k-1]['key'] == alphabet[i] and datas[k]['key'] == alphabet[j]:
            tmp.append(float(datas[k]['timestamp']) - float(datas[k-1]['timestamp']))
      if len(tmp) != 0:
        print(f"{ ( n + 1 ) }人目 { alphabet[i] }->{ alphabet[j] }, { len(tmp) }回, { sum(tmp) / len(tmp) }秒")
        pair_datas[n].append({'before_key': alphabet[i], 'after_key': alphabet[j], 'cnt': len(tmp), 'ave': ( sum(tmp) / len(tmp) )})
      else:
        print(f"{ ( n + 1 ) }人目 { alphabet[i] }->{ alphabet[j] }, 0回, 0秒")
        pair_datas[n].append({'before_key': alphabet[i], 'after_key': alphabet[j], 'cnt': 0, 'ave': 0})

# グラフ表示
fig, ax = plt.subplots()
fig.canvas.manager.set_window_title("前後のキーペアと所要時間の関係を表したグラフ")
for n in range(len(pair_datas)):
  glaph_data = []
  for data in pair_datas[n]:
    glaph_data.append(data['ave'])
  plt.plot(glaph_data, label="協力者" + str(n+1))
plt.xlabel("前後のキーペア")
plt.ylabel("平均時間(秒)")
plt.title("前後のキーペアと所要時間")
plt.legend(loc='upper right')
plt.show()