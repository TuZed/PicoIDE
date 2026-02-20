#import tkinter as tk
#import customtkinter as ctk

# App chia ra 3 phần
# State  : Lưu các thao tác, giá trị biến, lưu trữ thông tin
# Logic  : Nơi xử các thuật toán và lấy giá trị gửi giá trị về state
# UI/View: Nơi hiển thị đồ hoạ và đợi thao tác người dùng sử dụng Logic

#class AppState:
#    pass

#class AppLogic:
#    pass


#class AppView:
#    pass

#root = tk.Tk() #tạo cửa sổ
####

#root.title("RP2040-Editor")
#root.geometry("1280x720")
#root.resizable(True, True)


####
#root.mainloop()




import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton,
    QTextEdit, QLabel, QProgressBar, QListWidget
)
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QFont


class MiniIDE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini IDE Flasher")
        self.setMinimumSize(1000, 650)

        self.scripts = [
            "install_tools.bat",
            "setup_pico_sdk.bat",
            "add_path_auto_admin.bat",
            "verify_env.bat",
            "rebuild_clean.bat",
            "check_and_inject_serial.bat",
            "flash_if_rp2040_connected.bat"
        ]

        self.index = 0
        self.progress = 0

        self.init_ui()

    # ================= UI =================
    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout()
        central.setLayout(main_layout)

        # ===== Editor =====
        left_layout = QVBoxLayout()

        self.editor = QTextEdit()
        self.editor.setFont(QFont("Consolas", 11))
        self.editor.setPlaceholderText("Viết code C++ ở đây...")

        btn_layout = QHBoxLayout()
        self.save_btn = QPushButton("Save")
        self.flash_btn = QPushButton("Nạp")
        self.monitor_btn = QPushButton("Xem phản hồi mạch")

        btn_layout.addWidget(self.save_btn)
        btn_layout.addWidget(self.flash_btn)
        btn_layout.addWidget(self.monitor_btn)

        left_layout.addWidget(QLabel("Editor - code.cpp"))
        left_layout.addWidget(self.editor)
        left_layout.addLayout(btn_layout)

        main_layout.addLayout(left_layout, 3)

        # ===== Side =====
        right_layout = QVBoxLayout()

        self.progress_bar = QProgressBar()
        self.log_box = QListWidget()

        right_layout.addWidget(QLabel("Progress"))
        right_layout.addWidget(self.progress_bar)
        right_layout.addWidget(QLabel("Console"))
        right_layout.addWidget(self.log_box)

        main_layout.addLayout(right_layout, 1)

        # Signals
        self.save_btn.clicked.connect(self.save_code)
        self.flash_btn.clicked.connect(self.start_flash)
        self.monitor_btn.clicked.connect(self.start_monitor)

        # Timer cho progress giả
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

        self.apply_dark_theme()

    # ================= THEME =================
    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget { background-color: #0f1724; color: white; }
            QPushButton {
                background-color: #1f2937;
                border-radius: 8px;
                padding: 6px;
            }
            QPushButton:hover { background-color: #2563eb; }
            QTextEdit {
                background-color: #111827;
                border-radius: 8px;
            }
            QProgressBar {
                background-color: #1f2937;
                border-radius: 6px;
            }
            QProgressBar::chunk {
                background-color: #00b894;
                border-radius: 6px;
            }
        """)

    # ================= SAVE =================
    def save_code(self):
        with open("code.cpp", "w", encoding="utf-8") as f:
            f.write(self.editor.toPlainText())
        self.log("Saved code.cpp")

    # ================= FLASH =================
    def start_flash(self):
        self.index = 0
        self.log("Starting flash sequence...")
        self.run_next()

    def run_next(self):
        if self.index >= len(self.scripts):
            self.log("Flash sequence completed.")
            return

        script = self.scripts[self.index]

        if os.path.exists(script):
            self.log(f"Opening {script}")
            os.startfile(os.path.abspath(script))  
        else:
            self.log(f"{script} not found!")

        self.progress = 0
        self.progress_bar.setValue(0)
        self.timer.start(50)  # progress giả 5s

    def update_progress(self):
        self.progress += 1
        self.progress_bar.setValue(self.progress)

        if self.progress >= 100:
            self.timer.stop()
            self.index += 1
            QTimer.singleShot(5000, self.run_next)

    # ================= MONITOR =================
    def start_monitor(self):
        if os.path.exists("monitor.bat"):
            self.log("Opening monitor.bat")
            os.startfile(os.path.abspath("monitor.bat"))

        QTimer.singleShot(2000, self.open_monitor_exe)

    def open_monitor_exe(self):
        if os.path.exists("monitor.exe"):
            self.log("Opening monitor.exe")
            os.startfile(os.path.abspath("monitor.exe"))

    # ================= LOG =================
    def log(self, text):
        self.log_box.addItem(text)
        self.log_box.scrollToBottom()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MiniIDE()
    window.show()
    sys.exit(app.exec())

