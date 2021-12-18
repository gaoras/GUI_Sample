import tkinter as tk

# rootメインウインドウの設定
root = tk.Tk()
root.title("Sample")
root.geometry("250x100")

# メインフレームの作成と設置
frame = tk.Frame(root)
frame.pack(padx=20,pady=10)

# 各種ウィジェットの作成
myFrame = tk.Frame(frame, width=100, height=100, relief="solid", bd=1)

# 各種ウィジェットの設置
myFrame.pack(pady=20)

# メインループ
root.mainloop()