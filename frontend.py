import tkinter as tk
from tkinter import ttk
from backend import *

def submit():
    latitude_value = latitude_entry.get()
    longitude_value = longitude_entry.get()
    quality_value = quality_combobox.get()
    getStatistics(latitude_value, longitude_value, quality_value)

root = tk.Tk()
root.title('Solar App')

canvas = tk.Canvas(root, height=800, width=600)
canvas.pack()

background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Big label at the top
header_label = tk.Label(root, text="Your Solar Potential", font=('Helvetica', 20, 'bold'), bg='#4caf50', fg='white')
header_label.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.07)

frame = tk.Frame(root, bg='#ffffff', bd=5)

latitude_label = tk.Label(frame, text="Latitude:", font=('Helvetica', 12), bg='#ffffff')
latitude_label.grid(row=0, column=0, padx=(0, 5), pady=5, sticky=tk.E)

latitude_entry = tk.Entry(frame, font=('Helvetica', 12), bg='#f0f0f0')
latitude_entry.grid(row=0, column=1, padx=5, pady=5)

longitude_label = tk.Label(frame, text="Longitude:", font=('Helvetica', 12), bg='#ffffff')
longitude_label.grid(row=1, column=0, padx=(0, 5), pady=5, sticky=tk.E)

longitude_entry = tk.Entry(frame, font=('Helvetica', 12), bg='#f0f0f0')
longitude_entry.grid(row=1, column=1, padx=5, pady=5)

quality_label = tk.Label(frame, text="Quality:", font=('Helvetica', 12), bg='#ffffff')
quality_label.grid(row=2, column=0, padx=(0, 5), pady=5, sticky=tk.E)

quality_combobox = ttk.Combobox(frame, values=["LOW", "HIGH"], font=('Helvetica', 12), state='readonly', background='#f0f0f0')
quality_combobox.grid(row=2, column=1, padx=5, pady=5)
quality_combobox.set("HIGH")

submit_button = tk.Button(frame, text="Submit", command=submit, font=('Helvetica', 12, 'bold'), bg='#4caf50', fg='white')
submit_button.grid(row=3, column=0, columnspan=2, pady=5)

frame.place(relx=0.5, rely=0.45, relwidth=0.5, relheight=0.18, anchor='n')

root.resizable(width=False, height=False)
root.mainloop()
