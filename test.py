from pyautocad import Autocad

acad = Autocad(create_if_not_exists=True)

for obj in acad.iter_objects("hatch"):
	print(obj.ID)
