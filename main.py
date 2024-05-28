from tkinter import *
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  # Create a CTk window like you do with the Tk window

root.title('BMI-Calculator')
root.geometry('500x600')

# Logo
logo = ImageTk.PhotoImage(Image.open('images/bmi.jpg'))
logo_img = Label(root, image=logo, bd=0)
logo_img.pack(pady=20)

def clear_screen():
    h_entry.delete(0, END)
    w_entry.delete(0, END)
    results.configure(text='')

def get_bmi():
    # hitung BMI berat badan / tinggi badan ^2
    tinggi = float(h_entry.get())
    berat = float(w_entry.get())
    bmi = berat / (tinggi ** 2)
    bmi_rounded = round(bmi, 1)

    results.configure(text=f'{str(bmi_rounded)}')

    # Logic
    if bmi_rounded < 18.5:
        results.configure(text=f'{str(bmi_rounded)}\nKamu Kurus')
    elif bmi_rounded >= 18.5 and bmi_rounded <=24.9:
        results.configure(text=f'{str(bmi_rounded)}\nKamu Normal')
    elif bmi_rounded >= 25.0 and bmi_rounded <=29.9:
        results.configure(text=f'{str(bmi_rounded)}\nKamu Agak Gemuk')
    elif bmi_rounded > 30.0:
        results.configure(text=f'{str(bmi_rounded)}\nKamu Obesitas')
        

# Entry Box
h_entry = customtkinter.CTkEntry(
    master=root, 
    placeholder_text='Masukan Tinggi dengan Meter',
    width=200,
    height=30,
    border_width=1,
    corner_radius=10)
h_entry.pack(pady=20)

w_entry = customtkinter.CTkEntry(
    master=root, 
    placeholder_text='Masukan Berat dengan Kg',
    width=200,
    height=30,
    border_width=1,
    corner_radius=10)
w_entry.pack(pady=20)

# Button
button_1 = customtkinter.CTkButton(
    master=root,
    text='Hitung BMI',
    width=190,
    height=40,
    compound='top',
    command=get_bmi  # Perbaiki di sini
)
button_1.pack(pady=20)

button_2 = customtkinter.CTkButton(
    master=root,
    text='Hapus Halaman',
    width=190,
    height=40,
    fg_color='#D35B58',
    hover_color='#C77C78',
    command=clear_screen
)
button_2.pack(pady=20)

# Result
results = customtkinter.CTkLabel(
    master=root,
    text="",
)
results.pack(pady=50)

root.mainloop()
