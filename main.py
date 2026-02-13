import tkinter as tk

# App chia ra 3 phần
# State  : Lưu các thao tác, giá trị biến, lưu trữ thông tin
# Logic  : Nơi xử các thuật toán và lấy giá trị gửi giá trị về state
# UI/View: Nơi hiển thị đồ hoạ và đợi thao tác người dùng sử dụng Logic

class AppState:
    def __init__(self):
        self.value=0

class AppLogic:
    def __init__(self):
        self.state = AppState()

    def add(self):
        self.state.value+=1

    def sub(self):
        self.state.value-=1


class AppView:
    def __init__(self):
        #
        main_container = tk.Frame(root, bg="white")
        main_container.pack(expand=True, fill="both", padx=5, pady=5)
        #
        #
        centerText_container = tk.Frame(main_container, bg="gray")
        centerText_container.pack(side="top", expand=True, fill="both", padx=5, pady=5)

        centerBtn_container = tk.Frame(main_container, bg="gray")
        centerBtn_container.pack(side="top", expand=True, fill="both", padx=5, pady=5)
        #
        #
        text_container = tk.Frame(centerText_container, bg="black", padx=5, pady=5, width=400, height=200)
        text_container.pack_propagate(False)
        text_container.pack(expand=True, anchor="center")

        slogan = tk.Label(text_container, text="Số hiện tại là", font=("Arial", 14))
        slogan.pack(expand=True, fill="both")

        state_text = tk.Label(text_container, text="0", font=("Arial", 20))
        state_text.pack(expand=True, fill="both")
        #
        #
        left_container = tk.Frame(centerBtn_container, bg="Green")
        left_container.pack(side="left", expand=True, fill="both", padx=5, pady=5)

        left_btn =  tk.Button(left_container, text="ADD", width=40, height=5)
        left_btn.pack(expand=True, anchor="center")
        #
        #
        right_container = tk.Frame(centerBtn_container, bg="Red")
        right_container.pack(side="left", expand=True, fill="both", padx=5, pady=5)

        right_btn = tk.Button(right_container, text="SUB", width=40, height=5)
        right_btn.pack(expand=True, anchor="center")
        #

root = tk.Tk() #tạo cửa sổ
####

root.title("First app")
root.geometry("1280x720")
root.resizable(True, True)

AppView()

####
root.mainloop()
