import os

mshDir = os.listdir("msh")
for filename in mshDir:
	filenameNoExtension = os.path.splitext(filename)[0]
	os.system("dolfin-convert msh/" + filename + "msh/" + filenameNoExtension + ".xml")
