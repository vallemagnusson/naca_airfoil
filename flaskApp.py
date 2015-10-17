#!flask/bin/python
from celery import Celery
from celery import group
from flask import Flask, jsonify
import subprocess
import sys
import os
import swiftclient.client
import json
import time
from collections import Counter
import urllib2

app = Flask(__name__)

@app.route("/messaging", methods=['GET'])
def start():
	return "sidan fungerar", 200

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True )