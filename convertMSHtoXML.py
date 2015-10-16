import os

mshDir = os.listdir("msh")
for filename in mshDir:
	filenameNoExtension = os.path.splitext(filename)[0]
	oldFile = "msh/"+str(filename)
	newFile = "msh/" + filenameNoExtension + ".xml"
	os.system("dolfin-convert " + oldFile + " " + newFile)



#dolfin-convert cylinder6.msh out.xml