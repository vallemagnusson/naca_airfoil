import os

print os.listdir("msh")
os.system("dolfin-convert msh/r0a0n200.msh msh/out.xml")
