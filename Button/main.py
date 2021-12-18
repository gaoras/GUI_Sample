import tkinter as tk

def button_click(sender : tk.Button):
    sender.configure(text="clicked!")

def callback(event):
    print(event.widget["text"])

# rootメインウインドウの設定
root = tk.Tk()
root.title("Sample")
root.geometry("250x100")

# メインフレームの作成と設置
frame = tk.Frame(root)
frame.pack(padx=20,pady=10)

# 各種ウィジェットの作成
#button = tk.Button(frame, text="Button", command=button_click_command)         # command=func で書く場合は引数なしの関数になる  
button = tk.Button(frame, text="Button", command=lambda:button_click(button))   # command=lambda:func(args) の場合は自由な関数を設定できる

# イベントにバインドする方法
## <Button-1> 又は<1>:左クリック
## <Button-2> 又は<2>:ホイールクリック
## <Button-3> 又は<3>:右クリック
## <KeyPress-H> 又はh:hキー
## <Control-Shift-KeyPress-H>:Ctrl + Shift + h 入力
button.bind("<1>", callback)    

# 各種ウィジェットの設置
button.pack(pady=20)

# メインループ
root.mainloop()