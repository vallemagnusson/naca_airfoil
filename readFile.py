import os
import sys


def readFile(fileName):
	theFile = open(fileName, "r")
	print theFile
	for line in theFile:
		print line

readFile("navier_stokes_solver/results/drag_ligt.m")
