#!flask/bin/python

import os
import json
import time
#import swiftclient.client
import sys
import time
from celery import Celery
from collections import Counter
import urllib2

app = Celery('proj', backend='amqp', broker='amqp://mava:orkarinte@130.238.29.120:5672/app2')

@app.task
def convertFile(fileName, mshFile):
	print "test"
	print fileName
	if fileName == "r0a0n200.msh":
		newFile = open(fileName, "w")
		newFile.write(mshFile)
		newFile = open(fileName, "r")
		print newFile
		print newFile.read()
		newFile.close()
	return "dictionary_all"

@app.task
def readJSON(tweet_file):
	return "dictionary"
