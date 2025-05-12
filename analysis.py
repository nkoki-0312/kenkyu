filename = './datas/1747064422.952147.csv'  # 参照するファイル名。とりあえず直接指定。安定してデータが取れるようになったらまとめて取得とかも考えたい。
datas = []                                  # 読み込んだデータ
alphabet = "abcdefghijlkmnopqrstuvwxyz-"     # だたのアルファベット
left = "qwertasfghzxcvb"
right = "yuiop-hjklnm"

# データ取得
with open(filename, mode='r', encoding='utf-8') as f:
  while True:
    line = f.readline()
    if line == '':
      break

    line = line.split(",")
    datas.append({
      'key': line[0],
      'timestamp': line[1].replace('\n', '')
    })

# 前後の入力値とその時の所要時間
for i in range(len(datas)):
  if i != 0:
    if datas[i-1]['key'] != 'change' and datas[i]['key'] != 'change':
      print(f"{ datas[i-1]['key'] }->{ datas[i]['key'] }: { str( float(datas[i]['timestamp']) - float(datas[i-1]['timestamp']) ) }")

# 前後の入力値ごとの平均時間
tmp = []   # 特定のアルファベットの組み合わせの入力にかかる時間を保存しておく
for i in range(27):
  for j in range(27):
    tmp = []
    for k in range(len(datas)):
      if k != 0:
        if datas[k-1]['key'] == alphabet[i] and datas[k]['key'] == alphabet[j]:
          tmp.append(float(datas[k]['timestamp']) - float(datas[k-1]['timestamp']))
    if len(tmp) != 0:
      print(f"{ alphabet[i] }->{ alphabet[j] }, { len(tmp) }回, { sum(tmp) / len(tmp) }秒")

# 前後の入力値を左右どちらの手で入力するかで分ける
tmp = [[], []]   # 特定のアルファベットの組み合わせの入力にかかる時間を保存しておく
t = ["同", "違"]
onaji = []
chigau = []
for i in range(27):
  tmp = [[], []]
  for k in range(len(datas)):
    if k != 0:
      if datas[k-1]['key'] != 'change' and datas[k]['key'] == alphabet[i]:
        if ( datas[k-1]['key'] in left and datas[k]['key'] in left ) or ( datas[k-1]['key'] in right and datas[k]['key'] in right ):
          # 前後のアルファベットを同じ手で打つ場合
          tmp[0].append(float(datas[k]['timestamp']) - float(datas[k-1]['timestamp']))
          onaji.append(float(datas[k]['timestamp']) - float(datas[k-1]['timestamp']))
        else:
          # 前後のアルファベットを違う手で打つ場合
          tmp[1].append(float(datas[k]['timestamp']) - float(datas[k-1]['timestamp']))
          chigau.append(float(datas[k]['timestamp']) - float(datas[k-1]['timestamp']))
  for l in [0, 1]:
    if len(tmp[l]) != 0:
      print(f"{ t[l] }->{ alphabet[i] }, { len(tmp[l]) }回, { sum(tmp[l]) / len(tmp[l]) }秒")
print(f"前後を同じ手で打った場合の：平均 { sum(onaji) / len(onaji) }, 最小 { min(onaji) }, 最大 { max(onaji) }")
print(f"前後を違う手で打った場合の：平均 { sum(chigau) / len(chigau) }, 最小 { min(chigau) }, 最大 { max(chigau) }")