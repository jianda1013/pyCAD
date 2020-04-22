# -*- coding: utf-8 -*-

from pyautocad import Autocad, APoint
import math

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

count = acad.ActiveDocument.Layers.Count
layers_names = [acad.ActiveDocument.Layers.Item(i).Name for i in range(count)]

def count_layer():
	return count

def list_layer():
	return layers_names

def switch(name):
	acad.ActiveDocument.ActiveLayer = acad.ActiveDocument.Layers.Add(name)
	acad.ActiveDocument.Sendcommand("'_.-la"+chr(13)+"_on"+chr(13)+"="+name+chr(13)+chr(13))
	for i in range(count):
		if(layers_names[i] != name):
			acad.ActiveDocument.Sendcommand("'_.-la"+chr(13)+"_off"+chr(13)+"="+layers_names[i]+chr(13)+chr(13))
	# '_.-la _off =name

def recover():
	for i in range(count):
		acad.ActiveDocument.Sendcommand("'_.-la"+chr(13)+"_on"+chr(13)+"="+layers_names[i]+chr(13)+chr(13))


def hatch():
	acad.ActiveDocument.Sendcommand("h"+chr(13))