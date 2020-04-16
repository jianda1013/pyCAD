# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import cad


def pri():
	if(selection.get() == "直線"):

		def output():
			x1 = float(x1_input.get())
			y1 = float(y1_input.get())
			x2 = float(x2_input.get())
			y2 = float(y2_input.get())
			cad.LINE(x1, y1, x2, y2)
			x1_frame.destroy()
			y1_frame.destroy()
			x2_frame.destroy()
			y2_frame.destroy()
			toCAD.destroy()

		x1_frame = tk.Frame(window)
		x1_frame.grid(column=0, row=2)
		x1_pos = tk.Label(x1_frame, text=" 起始x座標 ")
		x1_pos.grid(column=0, row=2)
		x1_input = tk.Entry(x1_frame)
		x1_input.grid(column=1, row=2)

		y1_frame = tk.Frame(window)
		y1_frame.grid(column=0, row=3)
		y1_pos = tk.Label(y1_frame, text=" 起始y座標 ")
		y1_pos.grid(column=0, row=3)
		y1_input = tk.Entry(y1_frame)
		y1_input.grid(column=1, row=3)

		x2_frame = tk.Frame(window)
		x2_frame.grid(column=0, row=4)
		x2_pos = tk.Label(x2_frame, text=" 終點x座標 ")
		x2_pos.grid(column=0, row=4)
		x2_input = tk.Entry(x2_frame)
		x2_input.grid(column=1, row=4)

		y2_frame = tk.Frame(window)
		y2_frame.grid(column=0, row=5)
		y2_pos = tk.Label(y2_frame, text=" 終點y座標 ")
		y2_pos.grid(column=0, row=5)
		y2_input = tk.Entry(y2_frame)
		y2_input.grid(column=1, row=5)

		toCAD = tk.Button(window, text='確認送出', command=output)
		toCAD.grid(column=1, row=6)

	elif(selection.get() == "長方形"):

		def output():
			x = float(x_input.get())
			y = float(y_input.get())
			x_len = float(xlength_input.get())
			y_len = float(ylength_input.get())
			cad.REC(x, y, x_len, y_len)
			x_frame.destroy()
			y_frame.destroy()
			xlength_frame.destroy()
			ylength_frame.destroy()
			toCAD.destroy()

		x_frame = tk.Frame(window)
		x_frame.grid(column=0, row=2)
		x_pos = tk.Label(x_frame, text=" 起始x座標 ")
		x_pos.grid(column=0, row=2)
		x_input = tk.Entry(x_frame)
		x_input.grid(column=1, row=2)

		y_frame = tk.Frame(window)
		y_frame.grid(column=0, row=3)
		y_pos = tk.Label(y_frame, text=" 起始y座標 ")
		y_pos.grid(column=0, row=3)
		y_input = tk.Entry(y_frame)
		y_input.grid(column=1, row=3)

		xlength_frame = tk.Frame(window)
		xlength_frame.grid(column=0, row=4)
		x_length = tk.Label(xlength_frame, text=" x方向長度 ")
		x_length.grid(column=0, row=4)
		xlength_input = tk.Entry(xlength_frame)
		xlength_input.grid(column=1, row=4)

		ylength_frame = tk.Frame(window)
		ylength_frame.grid(column=0, row=5)
		y_length = tk.Label(ylength_frame, text=" y方向長度 ")
		y_length.grid(column=0, row=5)
		ylength_input = tk.Entry(ylength_frame)
		ylength_input.grid(column=1, row=5)

		toCAD = tk.Button(window, text='確認送出', command=output)
		toCAD.grid(column=1, row=6)

	elif(selection.get() == "圓形"):

		def output():
			x = float(x_input.get())
			y = float(y_input.get())
			radius = float(rad_input.get())
			cad.CIR(x, y, radius)
			x_frame.destroy()
			y_frame.destroy()
			rad_frame.destroy()
			toCAD.destroy()

		x_frame = tk.Frame(window)
		x_frame.grid(column=0, row=2)
		x_pos = tk.Label(x_frame, text=" 圓心x位置 ")
		x_pos.grid(column=0, row=2)
		x_input = tk.Entry(x_frame)
		x_input.grid(column=1, row=2)

		y_frame = tk.Frame(window)
		y_frame.grid(column=0, row=3)
		y_pos = tk.Label(y_frame, text=" 圓心y位置 ")
		y_pos.grid(column=0, row=3)
		y_input = tk.Entry(y_frame)
		y_input.grid(column=1, row=3)

		rad_frame = tk.Frame(window)
		rad_frame.grid(column=0, row=4)
		rad = tk.Label(rad_frame, text=" 輸入半徑 ")
		rad.grid(column=0, row=4)
		rad_input = tk.Entry(rad_frame)
		rad_input.grid(column=1, row=4)

		toCAD = tk.Button(window, text='確認送出', command=output)
		toCAD.grid(column=1, row=5)

	elif(selection.get() == "四分之一圓"):
		def output():
			x = float(x_input.get())
			y = float(y_input.get())
			radius = float(rad_input.get())
			start = arc_select.get()
			cad.QUA(x, y, radius, start)
			x_frame.destroy()
			y_frame.destroy()
			rad_frame.destroy()
			arc_frame.destroy()
			toCAD.destroy()

		x_frame = tk.Frame(window)
		x_frame.grid(column=0, row=2)
		x_pos = tk.Label(x_frame, text=" 圓心x位置 ")
		x_pos.grid(column=0, row=2)
		x_input = tk.Entry(x_frame)
		x_input.grid(column=1, row=2)

		y_frame = tk.Frame(window)
		y_frame.grid(column=0, row=3)
		y_pos = tk.Label(y_frame, text=" 圓心y位置 ")
		y_pos.grid(column=0, row=3)
		y_input = tk.Entry(y_frame)
		y_input.grid(column=1, row=3)

		rad_frame = tk.Frame(window)
		rad_frame.grid(column=0, row=4)
		rad = tk.Label(rad_frame, text=" 輸入半徑 ")
		rad.grid(column=0, row=4)
		rad_input = tk.Entry(rad_frame)
		rad_input.grid(column=1, row=4)

		arc_frame = tk.Frame(window)
		arc_frame.grid(column=0, row=5)
		arc_text = tk.Label(arc_frame, text=" 圓弧位置 ")
		arc_text.grid(column=0, row=5)
		arc_select = ttk.Combobox(arc_frame, values=["右上","左上","左下","右下"], state='readonly')
		arc_select.grid(column=1, row=5)
		toCAD = tk.Button(window, text='確認送出', command=output)
		toCAD.grid(column=1, row=6)



window = tk.Tk()
window.title('CAD_UI')
window.geometry('300x180')
window.configure(background='white')

cad_label = tk.Label(window, text='autocad')
cad_label.grid(column=0, row=0)

selection = ttk.Combobox(window, values=["直線","長方形","圓形","四分之一圓"], state='readonly')
selection.grid(column=0, row=1)
selection.current(0)

send_out = tk.Button(window, text='選擇', command=pri)
send_out.grid(column=1, row=1)


window.mainloop()