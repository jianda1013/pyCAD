import tkinter as tk
from tkinter import ttk

def pri():
	if(selection.get() == "直線"):
		
	else if(selection.get() == "長方形"):

	else if(selection.get() == "圓形"):

	else if(selection.get() == "四分之一圓"):




window = tk.Tk()
window.title('CAD_UI')
window.geometry('250x180')
window.configure(background='white')

cad_label = tk.Label(window, text='autocad')
cad_label.grid(column=0, row=0)

selection = ttk.Combobox(window, values=["直線","長方形","圓形","四分之一圓"], state='readonly')

selection.grid(column=0, row=1)
selection.current(0)

send_out = tk.Button(window, text='選擇', command=pri)
send_out.grid(column=1, row=1)

toCAD = tk.Button(window, text='確認送出')
toCAD.grid(column=1, row=5)


window.mainloop()