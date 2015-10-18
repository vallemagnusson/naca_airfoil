import sys
import os
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
	appLocation = app.root_path
	fileLocation = appLocation + "/msh/"
	content = sorted(os.listdir(fileLocation))
	print 1, fileLocation
	for i in range(len(content)):
		print content[i]
		if content[i] == "r3a9n200.msh":
			print open(fileLocation+content[i], "r").read()



test()