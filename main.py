import customtkinter as ctk
import yt_dlp
import threading
import os

def download_video():
    url = entry_url.get()
    if not url:
        status_label.configure(text="Vui lòng dán link vào!", text_color="red")
        return

    def run_download():
        try:
            status_label.configure(text="Đang tải...", text_color="yellow")
            btn_download.configure(state="disabled")
            
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'quiet': True
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            status_label.configure(text="Tải xong! Kiểm tra thư mục máy.", text_color="green")
        except Exception as e:
            status_label.configure(text=f"Lỗi: {str(e)}", text_color="red")
        finally:
            btn_download.configure(state="normal")

    # Chạy trong thread riêng để không bị treo giao diện
    threading.Thread(target=run_download).start()

# Cấu hình giao diện
app = ctk.CTk()
app.title("YouTube Downloader Pro")
app.geometry("500x250")

label = ctk.CTkLabel(app, text="Dán link YouTube vào đây:", font=("Arial", 16))
label.pack(pady=20)

entry_url = ctk.CTkEntry(app, width=400, placeholder_text="https://www.youtube.com/watch?v=...")
entry_url.pack(pady=10)

btn_download = ctk.CTkButton(app, text="Tải Xuống", command=download_video)
btn_download.pack(pady=20)

status_label = ctk.CTkLabel(app, text="")
status_label.pack()

app.mainloop()
