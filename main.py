import tkinter as tk

# App chia ra 3 phần
# State  : Lưu các thao tác, giá trị biến, lưu trữ thông tin
# Logic  : Nơi xử các thuật toán và lấy giá trị gửi giá trị về state
# UI/View: Nơi hiển thị đồ hoạ và đợi thao tác người dùng sử dụng Logic

class AppState:
    def __init__(self):
        self.value=1

class AppLogic:
    def __init__(self):
        self.state=AppState()

    def add(self):
        self.state.value += 1

    def sub(self):
        self.state.value -= 1

class AppView:
    def __init__(self, root, logic):
        self.logic=AppLogic()

        self.label=tk.Label(root, text="0")
        self.label.pack(pady=20)

        self.btn_add = tk.Button(root, text="Bam de tang", command=self.on_add)
        self.btn_add.pack(pady=20)
        self.btn_sub = tk.Button(root, text="Bam de giam", command=self.on_sub)
        self.btn_sub.pack(pady=20)

    def on_add(self):
        self.logic.add()
        self.label.config(text=str(self.logic.state.value))

    def on_sub(self):
        self.logic.sub()
        self.label.config(text=str(self.logic.state.value))


root = tk.Tk() #tạo cửa sổ
####

root.title("First app")
root.geometry("1280x720")
root.resizable(True, True)


logic = AppLogic()
view = AppView(root, logic)

####
root.mainloop()
