# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import cad

hatch_list = ["SOLID", "ANGLE", "ANSI31", "ANSI32", "ANSI33", "ANSI34", 
"ANSI35", "ANSI36", "ANSI37", "ANSI38", "AR-B816", "AR-B816C", "AR-B88", 
"AR-BRELM", "AR-BRSTD", "AR-CONC", "AR-HBONE", "AR-PARQ1", "AR-RROOF", 
"AR-RSHKE", "AR-SAND", "BOX", "BRASS", "BRICK", "BRSTONE", "CLAY", "CORK", 
"CROSS", "DASH", "DOLMIT", "DOTS", "EARTH", "ESCHER", "FLEX", "GOST_GLASS", 
"GOST_GROUND", "GOST_WOOD"]

def hide():
	but_frame.grid_forget()

def show():
	but_frame.grid()

def nlayer():
	def end():
		nlayer_frame.destroy()
		hch()

	hide()
	nlayer_frame = tk.Frame(window)
	nlayer_frame.grid(column=0, row=0)

	nlayer_name = tk.Label(nlayer_frame, text='新圖層名稱')
	nlayer_name.grid(column=0, row=0)

	nlayer_create = tk.Entry(nlayer_frame)
	nlayer_create.grid(column=0, row=1)

	nlayer_send = tk.Button(nlayer_frame, text='確認送出', command=lambda: [cad.switch(nlayer_create.get()),end()])
	nlayer_send.grid(column=1, row=1)

def hch():
	def end():
		cad.cal()
		hch_frame.destroy()
		show()

	hide()

	hch_frame = tk.Frame(window)
	hch_frame.grid(column=0, row=0)

	hch_choose = tk.Label(hch_frame, text="選取填充樣式")
	hch_choose.grid(column=0, row=0, padx=30, pady=10)

	hch_select = ttk.Combobox(hch_frame, values=hatch_list, state='readonly')
	hch_select.grid(column=0, row=1, padx=10, pady=10)

	hch_send = tk.Button(hch_frame, text='確認送出', command=lambda: [cad.set_hatch(hch_select.get()) ,cad.hatch(), end()])
	hch_send.grid(column=1, row=1, padx=5, pady=10)

window = tk.Tk()
window.title('CAD_UI')
window.geometry('250x100')
window.configure(background='white')

but_frame = tk.Frame(window)
but_frame.grid(column=0, row=0)

to_layer = tk.Label(but_frame, text='選擇圖層')
to_layer.grid(column=0, row=0,)

layer_selection = ttk.Combobox(but_frame, values=cad.list_layer(), state='readonly')
layer_selection.grid(column=0, row=1)

layer_send = tk.Button(but_frame, text='確認送出', command=lambda: [cad.switch(layer_selection.get()),hch()])
layer_send.grid(column=1, row=1)

layer_new = tk.Button(but_frame, text='創建新圖層', command=nlayer)
layer_new.grid(column=0, row=2, padx=30)

window.mainloop()