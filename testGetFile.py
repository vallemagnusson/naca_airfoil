import sys
import os
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
	print app.root_path

test()