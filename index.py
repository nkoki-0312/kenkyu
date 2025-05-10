import keyboard
import time

input_text = [{'key':'', 'timestamp':0.0}]

# 値取得
i = 1
while True:
  input_key = keyboard.read_key()
  if input_key != "":
    if input_key == 'esc':
      break
    input_text.append({'key':input_key, 'timestamp':time.time()})
    print(f"{i}: {input_text[i]}")
    i += 1

print(input_text)
before_after_pair = {}
for i, data in enumerate(input_text):
  if i == 0:
    continue
  before_key = data[i-1]['key']
  current_key = data[i]['key']
  timestamp = data[i]['timestamp']
  print(f"{before_key}, {current_key}, {timestamp}")