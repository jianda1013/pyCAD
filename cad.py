# -*- coding: utf-8 -*-

from pyautocad import Autocad, APoint
import math

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)


def list_layer():
	return [acad.ActiveDocument.Layers.Item(i).Name for i in range(acad.ActiveDocument.Layers.Count)]

def switch(name):
	acad.ActiveDocument.ActiveLayer = acad.ActiveDocument.Layers.Add(name)

def set_hatch(name):
	acad.ActiveDocument.Sendcommand("hpname"+chr(13)+name+chr(13))

def hatch():
	acad.ActiveDocument.Sendcommand("h"+chr(13))

def cal():
	arr = []
	for obj in acad.iter_objects("Hatch"):
		if(obj.Layer == acad.ActiveDocument.ActiveLayer.Name):
			arr.append(obj.Area)

	for obj in acad.iter_objects("PolyLine"):
		if(obj.Layer == acad.ActiveDocument.ActiveLayer.Name):
			x = (obj.Coordinates[0] + obj.Coordinates[2] + obj.Coordinates[4] + obj.Coordinates[6])/4
			y = (obj.Coordinates[1] + obj.Coordinates[3] + obj.Coordinates[5] + obj.Coordinates[7])/4
			start = str(x)+','+str(y)
			end = str(x)+','+str(y*2)
			acad.ActiveDocument.Sendcommand("mleader"+chr(13)+start+chr(13)+end+chr(13))
	print(arr)