import sys
import os
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
	appLocation = app.root_path
	fileLocation = appLocation + "/msh"
	print 1, fileLocation
	print 2, os.listdir(fileLocation)

test()