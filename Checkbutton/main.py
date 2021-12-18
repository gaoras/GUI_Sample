import tkinter as tk

def myCommand():
    print("myCommand!")

# rootメインウインドウの設定
root = tk.Tk()
root.title("Sample")
root.geometry("250x100")

# メインフレームの作成と設置
frame = tk.Frame(root)
frame.pack(padx=20,pady=10)

# 各種ウィジェットの作成
stv = tk.StringVar()
stv.set("0")
check_button = tk.Checkbutton(frame, text="CheckButton", command=myCommand, variable=stv)

button = tk.Button(frame, text="Button", command=lambda:print(stv.get()))


# 各種ウィジェットの設置
check_button.pack(pady=20)
button.pack()

# メインループ
root.mainloop()