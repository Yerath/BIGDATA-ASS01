#!/usr/bin/python
# coding=utf-8
import csv
import glob
import sys
import pymysql
import re

print "Importing StarSchema"

HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = ''
DATABASE = 'starschema'
UNIT_INIT = False

def executeSQL(sql):
	with connection.cursor() as cursor:
		cursor.execute(sql);
	connection.commit();

def getResult(sql):
	with connection.cursor() as cursor:
		cursor.execute(sql);
	connection.commit();
	return cursor.fetchone()

def getLastId():
	with connection.cursor() as cursor:
		cursor.execute("SELECT last_insert_id()")
	connection.commit();
	return cursor.fetchone()['last_insert_id()']

#Setup the connection
connection = pymysql.connect(host=HOSTNAME,
							 user=USERNAME,
							 password=PASSWORD,
							 db=DATABASE,
							 charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

#Enter all the presons into the database
f = open("../DATA/persons.csv", 'rt')
try: 
	reader = csv.reader(f)
	header = reader.next()

	for row in reader:
		sql = "INSERT INTO `Person` (`name`, `gender`, `birthdate`, `studentnr`) VALUES ('" + str(row[1]) + "', " + row[2] + ", '" + str(row[3]) + "', " + row[4] + ");"
		executeSQL(sql)
	
finally: 
	f.close()

print "Filling Blood Pressure"
#########################
# Blood Pressure
#########################
for filename in glob.glob('../DATA/bp*'):

	PERSON = str(re.findall('[A-Z][^A-Z]*',filename.strip('../DATA/bp').strip(".csv"))[0]) + " " + str(re.findall('[A-Z][^A-Z]*',filename.strip('../DATA/bp').strip(".csv"))[1])
	PERSON_ID = getResult("SELECT `idPerson` FROM `Person` WHERE `name` = '" + str(PERSON) + "'")["idPerson"]

	f = open(filename, 'rt')
	try:
		reader = csv.reader(f)
		header = reader.next()

		for row in reader:
			######################################
			# Create an Measurement for binding Quantity to it
			######################################
			sql = "INSERT INTO `Measurement_Facts` (`Person_idPerson`, `value`, `timestamp`, `phenomenon`, `phenomenon_type`,`unit`) VALUES (" + str(PERSON_ID) + ", '" + str(row[1]) +"', '"+ str(row[0]) +"', '', 'blood_pressure', '"+ str(header[1]) +"');"
			executeSQL(sql)

			######################################
			# Create an Measurement for binding Quantity to it
			######################################
			sql = "INSERT INTO `Measurement_Facts` (`Person_idPerson`, `value`, `timestamp`, `phenomenon`, `phenomenon_type`,`unit`) VALUES (" + str(PERSON_ID) + ", '" + str(row[2]) +"', '"+ str(row[0]) +"', '', 'blood_pressure', '"+ str(header[2]) +"');"
			executeSQL(sql)

	finally: 
		f.close()

print "Filling Heart Rate"
#########################
# Heart Rate
#########################
for filename in glob.glob('../DATA/bp*'):

	PERSON = str(re.findall('[A-Z][^A-Z]*',filename.strip('../DATA/bp').strip(".csv"))[0]) + " " + str(re.findall('[A-Z][^A-Z]*',filename.strip('../DATA/bp').strip(".csv"))[1])
	PERSON_ID = getResult("SELECT `idPerson` FROM `Person` WHERE `name` = '" + str(PERSON) + "'")["idPerson"]

	f = open(filename, 'rt')
	try:
		reader = csv.reader(f)
		header = reader.next()

		for row in reader:

			######################################
			# Create an Measurement for binding Quantity to it
			######################################
			sql = "INSERT INTO `Measurement_Facts` (`Person_idPerson`, `value`, `timestamp`, `phenomenon`, `phenomenon_type`,`unit`) VALUES (" + str(PERSON_ID) + ", '" + str(row[1]) +"', '"+ str(row[0]) +"', '', 'heart_rate', 'bpm');"
			executeSQL(sql)

	finally: 
		f.close()

print "Filling Temperature"
#########################
# Temperature
#########################

for filename in glob.glob('../DATA/bp*'):

	PERSON = str(re.findall('[A-Z][^A-Z]*',filename.strip('../DATA/bp').strip(".csv"))[0]) + " " + str(re.findall('[A-Z][^A-Z]*',filename.strip('../DATA/bp').strip(".csv"))[1])
	PERSON_ID = getResult("SELECT `idPerson` FROM `Person` WHERE `name` = '" + str(PERSON) + "'")["idPerson"]

	f = open(filename, 'rt')
	try:
		reader = csv.reader(f)
		header = reader.next()

		for row in reader:

			######################################
			# Create an Measurement for binding Quantity to it
			######################################
			sql = "INSERT INTO `Measurement_Facts` (`Person_idPerson`, `value`, `timestamp`, `phenomenon`, `phenomenon_type`,`unit`) VALUES (" + str(PERSON_ID) + ", '" + str(row[1]) +"', '"+ str(row[0]) +"', '', 'temperature', 'celcius');"
			executeSQL(sql)

	finally: 
		f.close()