# === 特定のファイルを句点(。)で区切る ===
# - 必要に応じてreplaceを増やすこと。
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

if __name__ == '__main__':
  input = './merosu.txt'
  output = './merosu.csv'

  # 文章を句点(。)で区切る
  separate(input, output)