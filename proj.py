#!flask/bin/python

import os
import json
import time
import sys
import time
import shutil
from celery import Celery
from collections import Counter
import urllib2
import subprocess

app = Celery('proj', backend='amqp', broker='amqp://mava:orkarinte@130.238.29.120:5672/app2')

@app.task
def convertFile(angle, n_nodes, n_levels, num_samples, visc, speed, T):
	print "Started to process file: "# + str(fileName)

	subprocess.call(["./run.sh", str(angle), str(angle), "1", n_nodes, n_levels])
	#appLocation = app.root_path
	fileLocation = "/home/ubuntu/naca_airfoil/msh/"
	content = sorted(os.listdir(fileLocation))
	fileName = "r" + n_levels + "a" + str(angle) + "n" + n_nodes + ".msh"
	#for i in content:
	#	if i == "r" + n_levels + "a" + angle + "n" + n_nodes + ".msh":
	#		fileName = content[i]
	##########################################
	##### Conver file from *msh to *.xml #####
	##########################################
	#newFile = open(fileName, "w")
	#newFile.write(mshFile)
	#newFile = open(fileName, "r")
	#newFile.close()
	fileNameWithoutExtension = os.path.splitext(fileName)[0]
	xmlFileName = fileNameWithoutExtension + ".xml"
	print fileNameWithoutExtension
	subprocess.call(["dolfin-convert", "msh/"+fileName, xmlFileName])
	##########################################
	########## Copy airfoil to dir ###########
	##########################################
	subprocess.call(["mkdir", fileNameWithoutExtension])
	subprocess.call(["cp", "-a", "airfoil", fileNameWithoutExtension])

	##########################################
	########## Run airfoil on file ###########
	##########################################
	num = str(num_samples)
	visc_s = str(visc)
	speed_s = str(speed)
	T_s = str(T)
	subprocess.call(["./airfoil", num, visc_s, speed_s, T_s, "../" + xmlFileName], cwd=fileNameWithoutExtension+"/")
	##########################################
	######### Get drag_ligt.m values #########
	##########################################
	resultLists = readFile("/home/ubuntu/naca_airfoil/" +fileNameWithoutExtension+"/results/drag_ligt.m")
	os.system("rm -rf " + fileNameWithoutExtension + "*")
	os.system("rm -rf  msh/*")
	os.system("rm -rf  geo/*")
	return (fileNameWithoutExtension+"N"+num+"v"+visc_s+"s"+speed_s+"T"+T_s+".msh", resultLists)
	
@app.task
def readFile(fileName):
	theFile = open(fileName, "r").read()
	timeColumn = []
	liftColumn = []
	dragColumn = []
	lines = open(fileName, "r").readlines()
	for x in range(1, len(lines)):
		time = lines[x].strip().split()[0]
		timeColumn.append(time)
		lift = lines[x].strip().split()[1]
		liftColumn.append(lift)
		drag = lines[x].strip().split()[2]
		dragColumn.append(drag)
	resultList = []
	resultList.append(timeColumn)
	resultList.append(liftColumn)
	resultList.append(dragColumn)
	return resultList








