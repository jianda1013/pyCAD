# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import cad

hatch_list = ["ANGLE", "ANSI31", "ANSI32", "ANSI33", "ANSI34", "ANSI37",
"AR-RROOF", "BOX", "BRASS", "BRICK", "BRSTONE", "CLAY", 
"CROSS","DOLMIT", "DOTS", "EARTH", "ESCHER", "FLEX", "GOST_GLASS", 
"GOST_GROUND", "GOST_WOOD"]

material_list = []

def layer():

	lst = cad.list_layer()
	def send():
		cad.switch(layer_selection.get())
		layer_frame.destroy()
		hch()

	layer_frame = tk.Frame(window)
	layer_frame.grid(column=0, row=0)

	layer_text = tk.Label(layer_frame, text='選擇所取圖層')
	layer_text.grid(column=0, row=0)

	layer_selection = ttk.Combobox(layer_frame, values=lst, state='readonly')
	layer_selection.grid(column=0, row=1)
	layer_selection.current(0)

	layer_send = tk.Button(layer_frame, text='確認送出', command=send)
	layer_send.grid(column=1, row=1)

	layer_new = tk.Button(layer_frame, text='開新圖層', command=lambda: [layer_frame.destroy(), nlayer()])
	layer_new.grid(column=0, row=2, padx=10, pady=0)

	layer_exit = tk.Button(layer_frame, text='結束並儲存', command=lambda: cad.exit())
	layer_exit.grid(column=1, row=3, padx=20, pady=10)

def nlayer():

	nlayer_frame = tk.Frame(window)
	nlayer_frame.grid(column=0, row=0)

	nlayer_text = tk.Label(nlayer_frame, text='新圖層名稱')
	nlayer_text.grid(column=0, row=0)

	nlayer_create = tk.Entry(nlayer_frame)
	nlayer_create.grid(column=0, row=1)

	nlayer_send = tk.Button(nlayer_frame, text='確認送出', command=lambda: [cad.switch(nlayer_create.get()), nlayer_frame.destroy(), hch()])
	nlayer_send.grid(column=1, row=1)

	nlayer_back = tk.Button(nlayer_frame, text='返回', command=lambda: [nlayer_frame.destroy(), layer()])
	nlayer_back.grid(column=1, row=2)

def hch():

	def send(num):
		cad.set_hatch(hatch_list[num])
		cad.hatch()
		hch_frame.destroy()
		comment()

	hch_frame = tk.Frame(window)
	hch_frame.grid(column=0, row=0)

	hch_text = tk.Label(hch_frame, text='選取材質')
	hch_text.grid(column=0, row=0)

	hch_select = ttk.Combobox(hch_frame, values=material_list, state='readonly')
	hch_select.grid(column=0, row=1)
	hch_select.current(0)

	hch_send = tk.Button(hch_frame, text='確認送出', command=lambda: [send(hch_select.current())])
	hch_send.grid(column=1, row=1)

	hch_mtl = tk.Button(hch_frame, text='新增材質', command=lambda: [hch_frame.destroy(), mtl()])
	hch_mtl.grid(column=0, row=2)

	hch_back = tk.Button(hch_frame, text='返回', command=lambda: [hch_frame.destroy(), layer()])
	hch_back.grid(column=1, row=2)

def mtl():

	def send(name):
		material_list.append(name)
		mtl_frame.destroy()
		hch()

	mtl_frame = tk.Frame(window)
	mtl_frame.grid(column=0, row=0)

	mtl_text = tk.Label(mtl_frame, text='輸入材質')
	mtl_text.grid(column=0, row=0)

	mtl_name = tk.Entry(mtl_frame)
	mtl_name.grid(column=0, row=1)

	mtl_send = tk.Button(mtl_frame, text='確認送出', command=lambda: [send(mtl_name.get())])
	mtl_send.grid(column=1, row=1)

def comment():
	comment_frame = tk.Frame(window)
	comment_frame.grid(column=0, row=0)

	comment_text = tk.Button(comment_frame, text='確認完成邊界處理', command=lambda: [comment_frame.destroy(), cad.cal(), layer()])
	comment_text.grid(column=0, row=0, padx=10, pady=10)

window = tk.Tk()
window.title('CAD_UI')
window.geometry('280x130')
window.configure(background='white')

layer()

window.mainloop()