import os
import sys


def readFile(fileName):
	theFile = open(fileName, "r").read()
	print theFile
	timeColumn = []
	print theFile.split()
	for line in theFile.split():
		timeColumn.append(line[0])
	#print timeColumn

readFile("navier_stokes_solver/results/drag_ligt.m")
