#!/usr/bin/python
###############################################################################
#
# Name: plot_file
# Arguments (0):
# 	
# Output: 
# Example:
###############################################################################
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os.path
import numpy as np

###############################################################################
# Takes a .m file that is created by the airfoil binary and creates a plot 
# from the data. Must be in the same directory as the .m file
# Arguments:
#	filename: Path o the file
###############################################################################
def plot_file(filename, data):
	#f = open("drag_ligt.m", "r")
	#s = f.read().split('\n')
	time = np.array(data[0])
	print 1
	lift = np.array(data[1])
	print 2
	drag = np.array(data[2])
	print 3
	#for line in s[1:]:
	#	l = line.split(' ')
	#	elemlist = []
	#	for element in l:
	#		if not element == "":
	#			elemlist.append(element)
	#	time.append(elemlist[0])
	#	drag.append(elemlist[1])
	#	lift.append(elemlist[2])
	plt.gca().set_color_cycle(['blue', 'red'])
	print 4
	plt.plot(time, drag)
	print 5
	plt.plot(time, lift)
	print 6
	plt.grid(True)
	print 7

	plt.legend(['Drag force', 'Lift force'])
	print 8
	plt.xlabel('Time')
	print 9
	plt.ylabel('Force')
	print 10
	plt.title(filename)
	print 11
	plt.yscale('log')
	print 12
	plt.savefig(os.path.splitext(filename)[0] + '.png')
	print 13
	#save("signal", ext="png", close=False, verbose=True)
	#image = open(os.path.splitext(filename)[0] + '.png', "w")
	#plt.savefig(image, format = "png")