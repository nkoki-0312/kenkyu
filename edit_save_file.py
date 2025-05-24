import os

DIR_PATH = "../収集データ"
SAVE_PATH = "./save_datas"
all_list = []
input_list = []
text_list = []

for p, personal_dir in enumerate(os.listdir(DIR_PATH)):
  tmp_all_list = []
  tmp_input_list = []
  tmp_text_list = []
  all_list.append([])
  input_list.append([])
  text_list.append([])
  for i, file in enumerate(os.listdir(DIR_PATH + "/" + personal_dir)):
    with open(DIR_PATH + "/" + personal_dir + "/" + file, mode="r", encoding="utf-8") as f:
      while True:
        row = f.readline()
        if row == '':
          break
        if i == 0:
          save_data = row.replace("\n", "")
          save_data = save_data.split(",")
          tmp_all_list.append(save_data)
        if i == 1:
          save_data = row.replace("\n", "")
          save_data = save_data.split(",")
          tmp_input_list.append(save_data)
        if i == 2:
          save_data = row.replace("\n", "")
          save_data = save_data.split(",")
          tmp_text_list.append(save_data)
  all_list[p].append(tmp_all_list)
  input_list[p].append(tmp_input_list)
  text_list[p].append(tmp_text_list)

for p in range(len(all_list)):
  with open(SAVE_PATH + "/all_" + str(p) + ".csv", mode="w", encoding="UTF-8") as f:
    # all
    for datas in all_list[p]:
      for data in datas:
        f.write(data[0] + "," + data[1] + "\n")
  with open(SAVE_PATH + "/input_" + str(p) + ".csv", mode="w", encoding="UTF-8") as f:
    # input
    for datas in input_list[p]:
      for data in datas:
        f.write(data[0] + "," + data[1] + "\n")
  with open(SAVE_PATH + "/text_" + str(p) + ".csv", mode="w", encoding="UTF-8") as f:
    # text
    for datas in text_list[p]:
      for data in datas:
        f.write(data[0] + "\n")

print("完了")