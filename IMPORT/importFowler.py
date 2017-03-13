#!/usr/bin/python
# coding=utf-8
import csv
import glob
import sys
import pymysql
import re

print "Importing Fowler"

HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = ''
DATABASE = 'fowler'

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
		cursor.execute("SELECT last_insert_id()");
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

#Create the phenomenon type
executeSQL("INSERT INTO `Phenomenon_Type` (`type`) VALUES('blood_pressure');")
PHENOMENON_TYPE = getLastId()

for filename in glob.glob('../DATA/bp*'):

	PERSON = str(re.findall('[A-Z][^A-Z]*',filename.strip('../DATA/bp').strip(".csv"))[0]) + " " + str(re.findall('[A-Z][^A-Z]*',filename.strip('../DATA/bp').strip(".csv"))[1])
	PERSON_ID = getResult("SELECT `idPerson` FROM `Person` WHERE `name` = '" + str(PERSON) + "'")["idPerson"]

	f = open(filename, 'rt')
	try:
		reader = csv.reader(f)
		header = reader.next()

		for row in reader:
			######################################
			# Create Observation and store that id
			######################################
			executeSQL("INSERT INTO `Observation` (`Person_idPerson`) VALUES (" + str(PERSON_ID) + ");")
			OBSERVATION_ID = getLastId()

			######################################
			# Insert the quantities of the measurements
			######################################
			sql = "INSERT INTO `Quantity` (`value`,`unit`) VALUES ('" + str(row[1]) + "','" + str(header[1]) + "');"
			executeSQL(sql)
			QUANTITY_ID = getLastId()

			######################################
			# Create an Measurement for binding Quantity to it
			######################################
			sql = "INSERT INTO `Measurement` (`Observation_idObservation`,`Phenomenon_Type_idPhenomenon_Type`,`Quantity_idQuanitity`,`timestamp`) VALUES (" + str(OBSERVATION_ID) + "," + str(PHENOMENON_TYPE) + "," + str(QUANTITY_ID) +"," + "'" + str(row[0]) + "');"
			executeSQL(sql)

			######################################
			# Insert the quantities of the measurements
			######################################
			sql = "INSERT INTO `Quantity` (`value`,`unit`) VALUES ('" + str(row[2]) + "','" + str(header[2]) + "');"
			executeSQL(sql)
			QUANTITY_ID = getLastId()

			######################################
			# Create an Measurement for binding Quantity to it
			######################################
			sql = "INSERT INTO `Measurement` (`Observation_idObservation`,`Phenomenon_Type_idPhenomenon_Type`,`Quantity_idQuanitity`,`timestamp`) VALUES (" + str(OBSERVATION_ID) + "," + str(PHENOMENON_TYPE) + "," + str(QUANTITY_ID) +"," + "'" + str(row[0]) + "');"
			executeSQL(sql)

			
	finally: 
		f.close()

print "Filling Heart Rate"
#########################
# Heart Rate
#########################

#Create the phenomenon type
executeSQL("INSERT INTO `Phenomenon_Type` (`type`) VALUES('heart_rate');")
PHENOMENON_TYPE = getLastId()

for filename in glob.glob('../DATA/hr*'):

	PERSON = str(re.findall('[A-Z][^A-Z]*',filename.strip('../DATA/bp').strip(".csv"))[0]) + " " + str(re.findall('[A-Z][^A-Z]*',filename.strip('../DATA/bp').strip(".csv"))[1])
	PERSON_ID = getResult("SELECT `idPerson` FROM `Person` WHERE `name` = '" + str(PERSON) + "'")["idPerson"]

	f = open(filename, 'rt')
	try:
		reader = csv.reader(f)
		header = reader.next()

		for row in reader:
			######################################
			# Create Observation and store that id
			######################################
			executeSQL("INSERT INTO `Observation` (`Person_idPerson`) VALUES (" + str(PERSON_ID) + ");")
			OBSERVATION_ID = getLastId()

			######################################
			# Insert the quantities of the measurements
			######################################
			sql = "INSERT INTO `Quantity` (`value`,`unit`) VALUES ('" + str(row[1]) + "','" + str(header[1]) + "');"
			executeSQL(sql)
			QUANTITY_ID = getLastId()

			######################################
			# Create an Measurement for binding Quantity to it
			######################################
			sql = "INSERT INTO `Measurement` (`Observation_idObservation`,`Phenomenon_Type_idPhenomenon_Type`,`Quantity_idQuanitity`,`timestamp`) VALUES (" + str(OBSERVATION_ID) + "," + str(PHENOMENON_TYPE) + "," + str(QUANTITY_ID) +"," + "'" + str(row[0]) + "');"
			executeSQL(sql)


	finally: 
		f.close()

print "Filling Temperature"
#########################
# Temperature
#########################

#Create the phenomenon type
executeSQL("INSERT INTO `Phenomenon_Type` (`type`) VALUES('temperature');")
PHENOMENON_TYPE = getLastId()

for filename in glob.glob('../DATA/temp*'):

	PERSON = str(re.findall('[A-Z][^A-Z]*',filename.strip('../DATA/bp').strip(".csv"))[0]) + " " + str(re.findall('[A-Z][^A-Z]*',filename.strip('../DATA/bp').strip(".csv"))[1])
	PERSON_ID = getResult("SELECT `idPerson` FROM `Person` WHERE `name` = '" + str(PERSON) + "'")["idPerson"]

	f = open(filename, 'rt')
	try:
		reader = csv.reader(f)
		header = reader.next()

		for row in reader:
			######################################
			# Create Observation and store that id
			######################################
			executeSQL("INSERT INTO `Observation` (`Person_idPerson`) VALUES (" + str(PERSON_ID) + ");")
			OBSERVATION_ID = getLastId()

			######################################
			# Insert the quantities of the measurements
			######################################
			sql = "INSERT INTO `Quantity` (`value`,`unit`) VALUES ('" + str(row[1]) + "','" + str(header[1]) + "');"
			executeSQL(sql)
			QUANTITY_ID = getLastId()

			######################################
			# Create an Measurement for binding Quantity to it
			######################################
			sql = "INSERT INTO `Measurement` (`Observation_idObservation`,`Phenomenon_Type_idPhenomenon_Type`,`Quantity_idQuanitity`,`timestamp`) VALUES (" + str(OBSERVATION_ID) + "," + str(PHENOMENON_TYPE) + "," + str(QUANTITY_ID) +"," + "'" + str(row[0]) + "');"
			print sql
			executeSQL(sql)


	finally: 
		f.close()