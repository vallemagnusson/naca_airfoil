import os
import sys


def readFile(fileName):
	theFile = open(fileName, "r").read()
	print theFile
	timeColumn = []
	for line in theFile:
		timeColumn.append(line[2])
		print timeColumn

readFile("navier_stokes_solver/results/drag_ligt.m")
