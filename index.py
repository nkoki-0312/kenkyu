import keyboard
import time

input_text = []

print("文字を入力してください")

# 値取得
i = 0
while True:
  input_key = keyboard.read_key()
  if input_key != "":
    if input_key == 'esc':
      break
    input_text.append({'key':input_key, 'timestamp':time.time()})
    print(f"{i}: {input_text[i]}")
    i += 1

print("----------")
print("結果")
before_timestamp = 0.0
text = ""
for i, data in enumerate(input_text):
  current_key = data['key']
  timestamp = data['timestamp']
  print(f"{current_key}, {timestamp-before_timestamp}")
  before_timestamp = timestamp
  if i % 2 == 0:
    text += current_key

print("----------")
print("入力された文字")
print(text)