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

def layer():
	def end():
		layer_frame.destroy()
		show()
	hide()

	layer_frame = tk.Frame(window)
	layer_frame.grid(column=0, row=0)

	layer_choose = tk.Label(layer_frame, text='選擇所取圖層')
	layer_choose.grid(column=0, row=0, padx=30, pady=10)

	layer_selection = ttk.Combobox(layer_frame, values=cad.list_layer(), state='readonly')
	layer_selection.grid(column=0, row=1, padx=10, pady=10)

	layer_send = tk.Button(layer_frame, text='確認送出', command=lambda: cad.switch(layer_selection.get()))
	layer_send.grid(column=1, row=1, padx=5, pady=10)

	but_end = tk.Button(layer_frame, text='結束選取圖層', command=end)
	but_end.grid(column=1, row=2, padx=5, pady=10)

def hch(name, framing):

	def end():
		hch_frame.destroy()
		show()

	cad.set_hatch(name)
	framing.destroy()

	hch_frame = tk.Frame(window)
	hch_frame.grid(column=0, row=0)

	hch_command = tk.Label(hch_frame, text='請移至autocad操作')
	hch_command.grid(column=0, row=0, padx=10, pady=30)

	hch_end = tk.Button(hch_frame, text='結束鑲嵌指令', command=end)
	hch_end.grid(column=0, row=1, padx=0, pady=0)

	cad.hatch()

def ch_2():
	hide()

	ch_2_frame = tk.Frame(window)
	ch_2_frame.grid(column=0, row=0)

	ch_2_choose = tk.Label(ch_2_frame, text="選取填充樣式")
	ch_2_choose.grid(column=0, row=0, padx=30, pady=10)

	ch_select = ttk.Combobox(ch_2_frame, values=hatch_list, state='readonly')
	ch_select.grid(column=0, row=1, padx=10, pady=10)

	ch_send = tk.Button(ch_2_frame, text='確認送出', command=lambda: hch(ch_select.get(), ch_2_frame))
	ch_send.grid(column=1, row=1, padx=5, pady=10)

window = tk.Tk()
window.title('CAD_UI')
window.geometry('300x180')
window.configure(background='white')

but_frame = tk.Frame(window)
but_frame.grid(column=0, row=0)
#1
to_layer = tk.Button(but_frame, text='選擇圖層', command=layer)
to_layer.grid(column=0, row=0, padx=10, pady=10)
#2
to_hatch = tk.Button(but_frame, text='使用鑲嵌', command=ch_2)
to_hatch.grid(column=1, row=0, padx=30, pady=10)

window.mainloop()