from pyautocad import Autocad
import openpyxl
from openpyxl import Workbook

acad = Autocad(create_if_not_exists=True)
wb = Workbook()
ws = wb.active

def total_area():
	x = 0
	y = 0
	for obj in acad.iter_objects("line"):
		if(obj.layer == "WALL"or"設計"):
			try:
				tmpx = int(abs(obj.delta[0]))
				tmpy = int(abs(obj.delta[1]))
				if(tmpx > x):
					x = tmpx
				if(tmpy > y):
					y = tmpy
			except:
				continue
	return x*y

start_pos = []
end_pos = []

for obj in acad.iter_objects("block"):
	if(obj.name == "圖框50%"):
		start_pos.append(str(int(obj.insertionpoint[0])-5)+','+str(int(obj.insertionpoint[1])-5))
		end_pos.append(str(int(obj.insertionpoint[0]+1230))+','+str(int(obj.insertionpoint[1]+905)))

for i in range(len(start_pos)):
	acad.ActiveDocument.SendCommand("copyclip"+chr(13)+start_pos[i]+chr(13)+end_pos[i]+chr(13)+chr(13))
	acad.ActiveDocument.SendCommand("erase"+chr(13)+"all"+chr(13)+chr(13))
	acad.ActiveDocument.SendCommand("pasteclip"+chr(13)+start_pos[i]+chr(13))
	lst = []
	for obj in acad.iter_objects("mleader"):
		if(obj.layer == "標注01-文字"):
			if obj.textstring not in lst:
				lst.append(obj.textstring)
	area_lst = [0, 0, 0]
	area = total_area()
	for obj in acad.iter_objects("polyline"):
		if(obj.layer == "8"):
			area_lst[0] += int(obj.area*2)
			area -= int(obj.area*2)
		elif(obj.layer == "WINDOW"):
			if(obj.closed == True):
				area -= int(obj.area)
		elif(obj.layer == "平-活動家具"):
			area -= int(obj.area)

	for obj in acad.iter_objects("hatch"):
		area -= int(obj.area)
		if(obj.patternname == "AR-RROOF"):
			area_lst[1] += int(obj.area)

	area_lst[2] = area

	dic = {}

	for i in range(len(lst)):
		if "壁紙" in lst[i]:
			dic[lst[i]] = area_lst[2]
		elif "鏡" in lst[i]:
			dic[lst[i]] = area_lst[1]
		elif "門片" in lst[i]:
			dic[lst[i]] = area_lst[0]

	print(dic)
	acad.ActiveDocument.SendCommand("u"+chr(13)+"u"+chr(13)+"u"+chr(13))

wb.save('temp.xlsx')
