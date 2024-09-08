import qrcode
from PIL import Image
import tkinter as tk
from tkinter import colorchooser, filedialog
from tkinter import ttk

class QRCodeGenerator:
    def __init__(self, qr_data, fill_color="blue", back_color="white", border=4, box_size=10):
        self.qr_data = qr_data
        self.fill_color = fill_color
        self.back_color = back_color
        self.border = border
        self.box_size = box_size

    def generate_qr(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=self.box_size,
            border=self.border,
        )
        qr.add_data(self.qr_data)
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color=self.fill_color, back_color=self.back_color).convert('RGBA')
        return qr_image

class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced QR Code Generator")
        self.root.configure(bg="white")

        # Set the window size
        self.root.geometry("600x400")

        self.qr_data = tk.StringVar()
        self.fill_color = "blue"
        self.back_color = "white"
        self.border = tk.IntVar(value=4)
        self.box_size = tk.IntVar(value=10)

        self.setup_gui()

    def setup_gui(self):
        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 12), background='white')
        style.configure('TButton', font=('Helvetica', 12), padding=10)
        style.configure('TEntry', font=('Helvetica', 12))

        container = tk.Frame(self.root, bg="white")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # Grid configuration
        container.grid_rowconfigure(0, weight=0)
        container.grid_rowconfigure(1, weight=0)
        container.grid_rowconfigure(2, weight=0)
        container.grid_rowconfigure(3, weight=0)
        container.grid_rowconfigure(4, weight=0)
        container.grid_rowconfigure(5, weight=0)
        container.grid_rowconfigure(6, weight=0)
        container.grid_rowconfigure(7, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

        tk.Label(container, text="Enter QR Code Data:", font=('Helvetica', 14), bg="white").grid(row=0, column=0, pady=(0, 10), sticky="w", columnspan=2)
        entry = ttk.Entry(container, textvariable=self.qr_data, width=60, font=('Helvetica', 14))
        entry.grid(row=1, column=0, columnspan=2, pady=(0, 10), sticky="ew")

        tk.Label(container, text="Border Size:", font=('Helvetica', 14), bg="white").grid(row=2, column=0, pady=(0, 5), sticky="w")
        border_spinbox = tk.Spinbox(container, from_=1, to=10, textvariable=self.border, font=('Helvetica', 12), width=5)
        border_spinbox.grid(row=2, column=1, pady=(0, 5), sticky="w")

        tk.Label(container, text="Box Size:", font=('Helvetica', 14), bg="white").grid(row=3, column=0, pady=(0, 5), sticky="w")
        box_size_spinbox = tk.Spinbox(container, from_=1, to=20, textvariable=self.box_size, font=('Helvetica', 12), width=5)
        box_size_spinbox.grid(row=3, column=1, pady=(0, 5), sticky="w")

        ttk.Button(container, text="Choose QR Code Color", command=self.choose_fill_color).grid(row=4, column=0, pady=(0, 10), sticky="w")
        ttk.Button(container, text="Choose Background Color", command=self.choose_back_color).grid(row=4, column=1, pady=(0, 10), sticky="w")
        ttk.Button(container, text="Generate QR Code", command=self.generate_qr).grid(row=5, column=0, columnspan=2, pady=(0, 20), sticky="w")

    def choose_fill_color(self):
        self.fill_color = colorchooser.askcolor(title="Choose QR Code Color")[1]

    def choose_back_color(self):
        self.back_color = colorchooser.askcolor(title="Choose Background Color")[1]

    def generate_qr(self):
        if not self.qr_data.get():
            return

        qr_generator = QRCodeGenerator(
            self.qr_data.get(), 
            self.fill_color, 
            self.back_color, 
            self.border.get(), 
            self.box_size.get()
        )
        qr_image = qr_generator.generate_qr()

        # Open save dialog
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            title="Save QR Code As"
        )

        if file_path:
            qr_image.save(file_path)
            tk.messagebox.showinfo("Success", f"QR Code saved to {file_path}")

        self.qr_data.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()
