# === 特定のファイルを句点(。)で区切る ===
def separate(input, output):
  with open(input, mode='r', encoding='utf-8') as rf:
    with open(output, mode='w', encoding='utf-8') as wf:
      text = rf.read()
      text = text.replace('　', '')
      text = text.replace('\n', '')
      text = text.replace('「', '')
      text = text.replace('」', '')
      text = text.replace('。', '\n')
      wf.write(text)

# === n文字以上の文章を除外 ===
def length_saver(input, output):
  with open(input, mode='r', encoding='utf-8') as rf:
    with open(output, mode='w', encoding='utf-8') as wf:
      while True:
        text = rf.readline()
        if text == '':
          break
        if len(text) <= 20:
          wf.write(text)

if __name__ == '__main__':
  input = './merosu.csv'
  output = './merosu_short.csv'

  # 文章を句点(。)で区切る
  # separate(input, output)

  # 20文字以上の文章を除外
  length_saver(input, output)