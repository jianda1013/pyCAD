# -*- coding: utf-8 -*-

from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

for obj in acad.iter_objects("PolyLine"):
    print(obj.Layer, obj.Coordinates)

for obj in acad.iter_objects("Hatch"):
	print(obj.PatternName, obj.Area)