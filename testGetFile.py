import sys
import os
import time

app = Flask(__name__)

@app.route('/')
def test():
	print app.root_path