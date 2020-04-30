# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import cad

hatch_list = ["ANGLE", "ANSI31", "ANSI32", "ANSI33", "ANSI34", "ANSI37",
"AR-RROOF", "BOX", "BRASS", "BRICK", "BRSTONE", "CLAY", 
"CROSS","DOLMIT", "DOTS", "EARTH", "ESCHER", "FLEX", "GOST_GLASS", 
"GOST_GROUND", "GOST_WOOD"]

material_list = ['灰鏡', '茶鏡', '門片', '上修門片']
main_list = ['客餐廳', '主臥', '兒子房', '次臥室']

def layer():

	def go(main, obj):
		cad.switch(main)
		cad.set_hatch(hatch_list[obj])
		cad.hatch()
		layer_frame.destroy()
		comment(obj)

	layer_frame = tk.Frame(window)
	layer_frame.grid(column=0, row=0, padx=20, pady=10)
	layer_frame.configure(background='white')

	main_text = tk.Label(layer_frame, text='主體大項')
	main_text.grid(column=0, row=0, padx=10, pady=10)
	main_text.configure(background='white')
	
	main_select = ttk.Combobox(layer_frame, value=main_list, state='readonly', width=10)
	main_select.grid(column=1, row=0, padx=10, pady=10)
	main_select.current(0)

	obj_text = tk.Label(layer_frame, text='細項品名')
	obj_text.grid(column=0, row=1)
	obj_text.configure(background='white')

	obj_select = ttk.Combobox(layer_frame, value=material_list, state='readonly', width=10)
	obj_select.grid(column=1, row=1)
	obj_select.current(0)

	sendout = tk.Button(layer_frame, text='Go', command=lambda:[go(main_select.get(), obj_select.current())])
	sendout.grid(column=2, row=1)
	sendout.configure(background='white')

def comment(num):
	comment_frame = tk.Frame(window)
	comment_frame.grid(column=0, row=0)
	comment_frame.configure(background='white')

	comment_text = tk.Button(comment_frame, text='邊界處理完成', command=lambda: [comment_frame.destroy(), cad.cal(num), layer()])
	comment_text.grid(column=0, row=0, padx=95, pady=30)
	comment_text.configure(background='white')

window = tk.Tk()
window.title('CAD_UI')
window.geometry('280x100+800+60')
window.configure(background='white')
window.resizable(False, False)


layer()


def on_closing():
	cad.exit()
	window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()