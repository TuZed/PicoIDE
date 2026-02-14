import tkinter as tk
import customtkiner as ctk

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
        pass

    def state_text_update(self, parent):
        self.text_state = tk.Label(parent, text="0", font=("Arial", 20))
        self.text_state.pack(expand=True, anchor="center", fill="both")

    def btn_view(self, parent, logic, text):
        self.parent = parent
        self.logic = logic

        self.btn = tk.Button(parent, text = str(text),  width=40, height=5, command=lambda: self.on_click(text) )
        self.btn.pack(expand=True, anchor="center")

    def on_click(self, text):
        if text=="ADD":
            self.logic.add()
            self.text_state.config(text=str(self.logic.state.value))
        else:
            self.logic.sub()
            self.text_state.config(text=str(self.logic.state.value))



root = tk.Tk() #tạo cửa sổ
####

root.title("First app")
root.geometry("1280x720")
root.resizable(True, True)

#
main_AppView = AppView()
logic_add_sub = AppLogic()

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

state_text_display = main_AppView
state_text_display.state_text_update(text_container)
#
#
left_container = tk.Frame(centerBtn_container, bg="Green")
left_container.pack(side="left", expand=True, fill="both", padx=5, pady=5)

left_btn = main_AppView
left_btn.btn_view(left_container, logic_add_sub, "ADD")
#
#
right_container = tk.Frame(centerBtn_container, bg="Red")
right_container.pack(side="left", expand=True, fill="both", padx=5, pady=5)

right_btn = main_AppView
right_btn.btn_view(right_container, logic_add_sub, "SUB")
#

####
root.mainloop()
