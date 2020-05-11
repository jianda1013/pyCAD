# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, messagebox
import cad

#def main():
#	main_frame = tk.Frame(window)
#	main_frame.grid()

	#main_select = ttk.Combobox(main_frame, values = cad.getgraph(), state = "readonly")
	#main_select.grid()

	#main_sentout = tk.Button(main_frame, text = "send", command = lambda: [main_frame.destroy(), loop(main_select.get())])
	#main_sentout.grid()

def loop():
	loop_frame = tk.Frame(window)
	loop_frame.grid()

	loop_select = ttk.Combobox(loop_frame, values = cad.leader_text(), state = "readonly")
	loop_select.grid()
	loop_select.current(1)


window = tk.Tk()
window.title('SING Design')
window.geometry('280x100+800+60')
window.configure(background = 'white')
window.resizable(False, False)

loop()

window.mainloop()