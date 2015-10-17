import os
import sys


def readFile(fileName):
	theFile = open(fileName, "r").read()
	#print theFile
	timeColumn = []
	lifeColumn = []
	dragColumn = []
	#print theFile.split()
	lines = open(fileName, "r").readlines()
	#with open(fileName, "r") as f:
		#content = f.readlines()
		#print content
	print lines[0]
	#for line in theFile.split():
	#	timeColumn.append(line[0])
	#print timeColumn

readFile("navier_stokes_solver/results/drag_ligt.m")
