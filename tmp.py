from pyautocad import Autocad, APoint


acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

# other

coner = [APoint(0, 40), APoint(0, 220), APoint(53, 40), APoint(53, 235), APoint(233, 40), APoint(233, 220), APoint(253, 40), APoint(253, 235)]
acad.model.AddLine(coner[0], coner[1])
acad.model.AddLine(coner[2], coner[3])
acad.model.AddLine(coner[4], coner[5])
acad.model.AddLine(coner[6], coner[7])
coner = [APoint(0, 0), APoint(0, 10), APoint(320, 0)]
acad.model.AddLine(coner[0], coner[1])
acad.model.AddLine(coner[0], coner[2])

acad.ActiveDocument.SendCommand("REC"+chr(13)+"73,40"+chr(13)+"193,220"+chr(10))

acad.ActiveDocument.SendCommand("REC"+chr(13)+"320,0"+chr(13)+"367,235"+chr(10))

acad.ActiveDocument.SendCommand("REC"+chr(13)+"0,220"+chr(13)+"320,235"+chr(10))

acad.ActiveDocument.SendCommand("REC"+chr(13)+"0,10"+chr(13)+"320,40"+chr(10))