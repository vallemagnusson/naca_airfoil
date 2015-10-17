import os
import sys


def readFile(fileName):
	theFile = open(fileName, "r")
	print theFile

readFile("navier_stokes_solver/results/drag_ligt.m")
