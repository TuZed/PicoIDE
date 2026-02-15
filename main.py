import subprocess
import os

class AppView:
    def create_button(self, parent, text, batch_file):
        self.btn = ctk.CTkButton(
            parent,
            text=text,
            command=lambda: self.run_batch(batch_file)
        )
        self.btn.pack()

    def run_batch(self, batch_file):
        try:
            # Kiểm tra file tồn tại
            if not os.path.exists(batch_file):
                print(f"❌ Không tìm thấy {batch_file}")
                return

            # Chạy file batch
            subprocess.Popen([batch_file], shell=True)
            print(f"✅ Đang chạy {batch_file}")

        except Exception as e:
            print(f"❌ Lỗi: {e}")
