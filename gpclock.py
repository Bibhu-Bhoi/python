import tkinter as tk
from time import strftime

def update_time():
    time_string = strftime('%H:%M:%S %p')
    time_label.config(text=time_string)
    time_label.after(1000, update_time)
window = tk.Tk()
window.title("Digital Clock")
time_label = tk.Label(window, font=('Arial', 80), bg='black', fg='blue')
time_label.pack(pady=50)
update_time()
window.mainloop()
