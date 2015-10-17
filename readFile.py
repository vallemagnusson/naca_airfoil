import os
import sys
import matplotlib.pyplot as plt

def readFile(fileName):
	theFile = open(fileName, "r").read()
	#print theFile
	timeColumn = []
	liftColumn = []
	dragColumn = []
	#print theFile.split()
	lines = open(fileName, "r").readlines()
	#with open(fileName, "r") as f:
		#content = f.readlines()
		#print content
	for x in range(1, len(lines)):
		time = lines[x].strip().split()[0]
		timeColumn.append(time)
		lift = lines[x].strip().split()[1]
		liftColumn.append(lift)
		drag = lines[x].strip().split()[2]
		dragColumn.append(drag)
	print timeColumn
	print liftColumn
	print dragColumn
		#print lines[x].strip()
	#for line in theFile.split():
	#	timeColumn.append(line[0])
	#print timeColumn
	plt.plot(timeColumn, liftColumn)
	plt.show()

readFile("navier_stokes_solver/results/drag_ligt.m")
