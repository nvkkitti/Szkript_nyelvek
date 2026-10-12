import tkinter as tk
from tkinter import ttk
import random

def dobas():
    szam = random.randint(1, 6)
    dobas_eredmenye.config(text=szam)

root = tk.Tk()
root.title("Kockázás")
root.geometry("600x400")
# root.minsize(500, 300)
# root.maxsize(800, 500)
# root.resizable(False, False)

cim_cimke = ttk.Label(root, text='Kockajáték', font='Arial 16 bold')
cim_cimke.pack(pady=(20, 10))

dobas_szam = tk.StringVar(value="10")
dobas_szam_be = ttk.Entry(root, textvariable=dobas_szam, width=10)
dobas_szam_be.pack(pady=5)

dobas_gomb = ttk.Button(root, text='Dobás', command=dobas)
dobas_gomb.pack(pady=5)

dobas_eredmenye = ttk.Label(root, text='Eredmény', font='Arial 16 bold')
dobas_eredmenye.pack(pady=10)

kilepes_gomb = ttk.Button(root, text='Kilépés', command=root.destroy)
kilepes_gomb.pack(pady=5)

root.mainloop()