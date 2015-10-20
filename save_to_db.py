import pickledb
import sys
import os

def to_db(key, value):
	dataBaseName = "database"
	db = pickledb.load(dataBaseName, False)
	dbKeys = db.getall()
	if key not in dbKeys:
		print 1, "Ny grej"
		db.set(key, value)
		db.dump()

def in_db(fileName):
	dataBaseName = "database"
	db = pickledb.load(dataBaseName, False)
	dbKeys = db.getall()
	if fileName in dbKeys:
		print "Already in db!"
	else:
		return fileName