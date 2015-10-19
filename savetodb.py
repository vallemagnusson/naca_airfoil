import pickledb
import sys
import os

def save_to_db(key, value):
	dataBaseName = "database"
	db = pickledb.load(dataBaseName, False)
	dbKeys = db.getall()
	if key not in dbKeys:
		print 1, "Ny grej"
		db.set(key, value)
		db.dump()