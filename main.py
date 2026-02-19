import tkinter as tk
import customtkinter as ctk

# App chia ra 3 phần
# State  : Lưu các thao tác, giá trị biến, lưu trữ thông tin
# Logic  : Nơi xử các thuật toán và lấy giá trị gửi giá trị về state
# UI/View: Nơi hiển thị đồ hoạ và đợi thao tác người dùng sử dụng Logic

class AppState:
    pass

class AppLogic:
    pass


class AppView:
    pass

root = tk.Tk() #tạo cửa sổ
####

root.title("RP2040-Editor")
root.geometry("1280x720")
root.resizable(True, True)


####
root.mainloop()
