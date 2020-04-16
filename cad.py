# -*- coding: utf-8 -*-

from pyautocad import Autocad, APoint
import math

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

def LINE(pos_x, pos_y, des_x, des_y):
	start = APoint(pos_x, pos_y)
	end = APoint(des_x, des_y)
	acad.model.Addline(start, end)

def REC(pos_x, pos_y, x_length, y_length):
	pos_str = str(pos_x)+","+str(pos_y)
	des_x = pos_x + x_length
	des_str = str(pos_x+x_length)+","+str(pos_y+y_length)
	acad.ActiveDocument.SendCommand("REC"+chr(13)+pos_str+chr(13)+des_str+chr(10))

def CIR(pos_x, pos_y, radius):
	center = APoint(pos_x, pos_y)
	acad.model.AddCircle(center, radius)

def QUA(pos_x, pos_y, radius, start):
	center = APoint(pos_x, pos_y)
	if(start == "右上"):
		acad.model.AddArc(center, radius, math.radians(0), math.radians(90))
	elif(start == "左上"):
		acad.model.AddArc(center, radius, math.radians(90), math.radians(180))
	elif(start == "左下"):
		acad.model.AddArc(center, radius, math.radians(180), math.radians(270))
	elif(start == "右下"):
		acad.model.AddArc(center, radius, math.radians(270), math.radians(0))

def UNDO():
	acad.ActiveDocument.SendCommand("undo"+chr(13)+"1"+chr(10))

