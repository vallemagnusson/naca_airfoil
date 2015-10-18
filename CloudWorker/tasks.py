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

app = Celery('tasks', backend='amqp', broker='amqp://mava:orkarinte@130.238.29.120:5672/app2')

@app.task
def getTweets(tweetFileList):
	
	return "dictionary_all"

@app.task
def readJSON(tweet_file):
	return "dictionary"
