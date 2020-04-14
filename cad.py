from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

def REC(pos_x, pos_y, x_length, y_length):
	pos_str = str(pos_x)+","+str(pos_y)
	des_x = pos_x + x_length
	des_str = str(pos_x+x_length)+","+str(pos_y+y_length)
	acad.ActiveDocument.SendCommand("REC"+chr(13)+pos_str+chr(13)+des_str+chr(10))

def LINE(pos_x, pos_y, des_x, des_y):
	start = APoint(pos_x, pos_y)
	end = APoint(des_x, des_y)
	acad.model.Addline(start, end)