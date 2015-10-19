#!flask/bin/python

from flask import Flask, jsonify, request, render_template, url_for
from celery import group
import sys
import os
import time
from proj import convertFile
import subprocess

app = Flask(__name__, template_folder="/home/ubuntu/naca_airfoil")

@app.route('/')
def form():
	return render_template('form_submit.html')

@app.route('/runsh/', methods=['POST'])
def runsh():
	angle_start=request.form['angle_start']
	angle_stop=request.form['angle_stop']
	n_angles=request.form['n_angles']
	n_nodes=request.form['n_nodes']
	n_levels=request.form['n_levels']
	print 1, "- - - - - - - - Run start - - - - - - - -"
	########################
	##### Create *.msh #####
	########################
	start_time_to_make_msh_file = time.time()
	os.system("./run.sh " + angle_start + " " + angle_stop + " " + n_angles + " " + n_nodes + " " + n_levels)
	stop_time_to_make_msh_file = time.time()
	time_to_make_msh_file = stop_time_to_make_msh_file - start_time_to_make_msh_file
	print 2, time_to_make_msh_file
	print 3, app.root_path
	##################################
	##### Convert *.msh to *.xml #####
	##################################

	appLocation = app.root_path
	print 4, "Fel"
	fileLocation = appLocation + "/msh/"
	print 5, "Fel"
	content = sorted(os.listdir(fileLocation))
	print 6, "Fel"
	response = group(convertFile.s(fileName, open(fileLocation+fileName, "r").read()) for fileName in content)
	print 7, "Fel"
	result = response.apply_async()
	print 8, "Fel"
	print result
	print result.get()
	result.get()
	print 9, "Fel"
	#for i in range(len(content)):
	#	print content[i]
	#	fileContent = open(fileLocation+content[i], "r").read()
	#	#print fileContent
	#	response = group()
	#	convertFile(content[i], fileContent)
	for t in result.get():
		print t
	subprocess.call(["rm", "-rf", "*.msh"], cwd="msh/")
	return render_template('runsh.html', 
							angle_start=angle_start, 
							angle_stop=angle_stop, 
							n_angles=n_angles, 
							n_nodes=n_nodes, 
							n_levels=n_levels)


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True )