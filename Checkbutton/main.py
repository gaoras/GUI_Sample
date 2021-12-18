import tkinter as tk

def button_click(sender : tk.Button):
    sender.configure(text="clicked!")



# rootメインウインドウの設定
root = tk.Tk()
root.title("Sample")
root.geometry("250x100")

# メインフレームの作成と設置
frame = tk.Frame(root)
frame.pack(padx=20,pady=10)

# 各種ウィジェットの作成
check_button = tk.Checkbutton(frame, text="CheckButton")

# 各種ウィジェットの設置
check_button.pack(pady=20)

# メインループ
root.mainloop()