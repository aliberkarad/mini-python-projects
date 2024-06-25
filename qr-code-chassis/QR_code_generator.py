import tkinter as tk
from tkinter import messagebox
import random
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageTk

class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("300x100")

        self.label = tk.Label(root, text="Kaç QR kodu oluşturmak istiyorsunuz?")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.generate_button = tk.Button(root, text="QR Kodları Oluştur", command=self.generate_qr_codes)
        self.generate_button.pack()

        self.result_frame = tk.Frame(root)
        self.result_frame.pack()

    def generate_qr_codes(self):
        try:
            num_qr_codes = int(self.entry.get())
            if num_qr_codes <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Hata", "Geçersiz giriş. Lütfen pozitif bir tam sayı girin.")
            return

        self.clear_result_frame()

        for _ in range(num_qr_codes):
            name = self.generate_name()
            qr_code = self.generate_qr_code(name)
            qr_with_logo = self.add_logo_to_qr(qr_code)
            self.save_qr_code_with_text(name, qr_with_logo)

    def generate_name(self):
        allowed_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        return ''.join(random.choices(allowed_characters, k=4))

    def generate_qr_code(self, data):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction to accommodate logo
            box_size=10,
            border=4,
        )
        data = f"https://sharing.5kkaravan.com/QRs/{data}.html"
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        return img

    def add_logo_to_qr(self, qr_code):
        logo = Image.open("C:/Users/Ali Berkay Karadeniz/5K.jpg").convert("RGBA")  # Logonun yolu ve RGBA moduna dönüştürme
        qr_code = qr_code.convert("RGBA")

        # Logonun boyutunu ayarla
        basewidth = 100
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.LANCZOS)

        # Logoyu QR kodunun ortasına yerleştir
        pos = ((qr_code.width - basewidth) // 2 , (qr_code.height - hsize) // 2)
        qr_code.paste(logo, pos)

        return qr_code

    def save_qr_code_with_text(self, name, qr_code):
        text = name  # Eklenecek metin
        draw = ImageDraw.Draw(qr_code)
        font = ImageFont.truetype("verdana.ttf", 20)  # Kullanılacak font ve boyut
        text_bbox = draw.textbbox((0, 0), text, font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        position = ((qr_code.width - text_width) // 2, qr_code.height - text_height - 20)
        draw.text(position, text, fill="black", font=font)  # Metni QR kodunun alt kısmına yerleştir
        qr_code.save(f"{name}.png")

    def clear_result_frame(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
