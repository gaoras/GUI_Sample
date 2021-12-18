import tkinter as tk

# rootメインウインドウの設定
root = tk.Tk()
root.title("Sample")
root.geometry("250x100")

# メインフレームの作成と設置
frame = tk.Frame(root)
frame.pack(padx=20,pady=10)

# 各種ウィジェットの作成
entryText = tk.StringVar()
entry = tk.Entry(frame, textvariable=entryText)

button = tk.Button(frame, text="Button", command=lambda:print(entryText.get()))

# 各種ウィジェットの設置
entry.pack(pady=20)
button.pack()

# メインループ
root.mainloop()