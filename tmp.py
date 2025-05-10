import tkinter as tk
import keyboard

keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

# ウィンドウ作成
root = tk.Tk()
root.title('タイピングの癖を用いた個人認証システム')
root.geometry('640x480')

input_text = ""

debug_win = tk.Toplevel()
debug_win.title('Debug')
debug_win.geometry("300x480")

# https://qiita.com/nnahito/items/ad1428a30738b3d93762を見ながら作成する
text = tk.Label(text='文字を入力してください。', font=('Noto Sans JP', 16), foreground='#555555')
text.place(x=8, y=8)

# ウィンドウを表示
root.mainloop()

i = 0
while True:
  input_key = keyboard.read_key()
  if input_key != "":
    if input_key == 'space':
      break

    print(input_text)
    input_text += input_key
    display_debug = tk.Label(text=input_text, font=('Noto Sans JP', 16), foreground='#555555')
    display_debug.place(x=8, y=128 + (64*i))
    i += 1