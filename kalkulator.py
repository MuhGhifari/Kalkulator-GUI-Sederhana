import tkinter as tk  # Import library Tkinter untuk membuat GUI
from tkinter import messagebox  # Import messagebox dari Tkinter untuk menampilkan pesan kesalahan
from tkinter import Button

class Calculator:
    def __init__(self, root):
        self.root = root  # Inisialisasi jendela utama
        self.root.title("Calculator")  # Set judul jendela
        self.root.geometry("400x600")  # Set ukuran jendela
        self.current_input = ""  # Menyimpan input saat ini
        
        self.display_frame = self.create_display_frame()  # Membuat frame untuk display
        self.buttons_frame = self.create_buttons_frame()  # Membuat frame untuk tombol

        self.display_label = self.create_display_label()  # Membuat label untuk display

        self.create_digit_buttons()  # Membuat tombol digit
        self.create_operator_buttons()  # Membuat tombol operator
        self.create_special_buttons()  # Membuat tombol spesial seperti clear dan equals

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=221, bg="lightgray")  # Membuat frame untuk display dengan background lightgray
        frame.pack(expand=True, fill="both")  # Mengatur agar frame mengisi ruang yang tersedia
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)  # Membuat frame untuk tombol
        frame.pack(expand=True, fill="both")  # Mengatur agar frame mengisi ruang yang tersedia
        return frame

    def create_display_label(self):
        label = tk.Label(self.display_frame, text="", anchor=tk.E, bg="white", fg="black", padx=24, font=("Arial", 40))  # Membuat label untuk display dengan beberapa properti
        label.pack(expand=True, fill="both")  # Mengatur agar label mengisi ruang yang tersedia
        return label

    def add_to_expression(self, value):
        self.current_input += str(value)  # Menambahkan nilai ke input saat ini
        self.update_display()  # Memperbarui tampilan

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():  # Membuat tombol digit berdasarkan nilai dalam dictionary
            button = tk.Button(self.buttons_frame, text=str(digit), bg="white", fg="black", font=("Arial", 24), borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)  # Menempatkan tombol dalam grid

    def create_operator_buttons(self):
        for operator, grid_value in self.operators.items():  # Membuat tombol operator berdasarkan nilai dalam dictionary
            button = tk.Button(self.buttons_frame, text=operator, bg="white", fg="red", font=("Arial", 24), borderwidth=0, command=lambda x=operator: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)  # Menempatkan tombol dalam grid

    def clear(self):
        self.current_input = ""  # Menghapus input saat ini
        self.update_display()  # Memperbarui tampilan

    def create_special_buttons(self):
        self.create_clear_button()  # Membuat tombol clear
        self.create_equals_button()  # Membuat tombol equals

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg="white", fg="red", font=("Arial", 24), borderwidth=0, command=self.clear)  # Membuat tombol clear dengan properti tertentu
        button.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)  # Menempatkan tombol dalam grid

    def evaluate_expression(self):
        try:
            self.current_input = str(eval(self.current_input))  # Mengevaluasi ekspresi matematika dalam input saat ini
            self.update_display()  # Memperbarui tampilan
        except Exception as e:
            self.current_input = ""  # Jika terjadi kesalahan, hapus input saat ini
            messagebox.showerror("Error", "Invalid Expression")  # Tampilkan pesan kesalahan
            self.update_display()  # Memperbarui tampilan

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="white", fg="red", font=("Arial", 24), borderwidth=0, command=self.evaluate_expression)  # Membuat tombol equals dengan properti tertentu
        button.grid(row=0, column=2, columnspan=2, sticky=tk.NSEW)  # Menempatkan tombol dalam grid

    def update_display(self):
        self.display_label.config(text=self.current_input)  # Memperbarui teks dalam label display

    def configure_grid(self):
        for i in range(5):  # Konfigurasi grid untuk frame tombol
            self.buttons_frame.rowconfigure(i, weight=1)  # Atur bobot baris
            self.buttons_frame.columnconfigure(i, weight=1)  # Atur bobot kolom

    digits = {
        7: (1, 0), 8: (1, 1), 9: (1, 2),
        4: (2, 0), 5: (2, 1), 6: (2, 2),
        1: (3, 0), 2: (3, 1), 3: (3, 2),
        0: (4, 1),
    }  # Dictionary untuk digit dan posisi gridnya

    operators = {
        "/": (1, 3),
        "*": (2, 3),
        "-": (3, 3),
        "+": (4, 3)
    }  # Dictionary untuk operator dan posisi gridnya

if __name__ == "__main__":
    root = tk.Tk()  # Inisialisasi jendela utama Tkinter
    calculator = Calculator(root)  # Membuat objek kalkulator
    calculator.configure_grid()  # Konfigurasi grid untuk frame tombol
    root.mainloop()  # Memulai loop utama Tkinter