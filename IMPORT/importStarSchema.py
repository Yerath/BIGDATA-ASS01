#!/usr/bin/python
# coding=utf-8
import csv
import glob
import sys
import pymysql
import re

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
		print sql
		executeSQL(sql)
	
finally: 
	f.close()

#########################
# Blood Pressure
#########################

#Create the phenomenon type
executeSQL("INSERT INTO `Phenomenon_type` (`name`) VALUES('blood_pressure');")
PHENOMENON_TYPE = getLastId()

#Create Dummy phenomenon
executeSQL("INSERT INTO `Phenomenon` (`name`) VALUES('group A');")
PHENOMENON = getLastId()

#Create units
executeSQL("INSERT INTO `Unit` (`name`) VALUES ('diastolic')");
DIASTOLIC_ID = getLastId()

executeSQL("INSERT INTO `Unit` (`name`) VALUES ('systolic')");
SYSTOLIC_ID = getLastId()

for filename in glob.glob('../DATA/bp*'):

	PERSON = str(re.findall('[A-Z][^A-Z]*',filename.strip('../DATA/bp').strip(".csv"))[0]) + " " + str(re.findall('[A-Z][^A-Z]*',filename.strip('../DATA/bp').strip(".csv"))[1])
	print PERSON
	PERSON_ID = getResult("SELECT `idPerson` FROM `Person` WHERE `name` = '" + str(PERSON) + "'")["idPerson"]

	f = open(filename, 'rt')
	try:
		reader = csv.reader(f)
		header = reader.next()

		for row in reader:
			######################################
			# Create an Measurement for binding Quantity to it
			######################################
			sql = "INSERT INTO `Measurement_Facts` (`Phenomenon_type_idPhenomenon`,`Person_idPerson`,`Unit_idUnit`,`Phenomenon_idPhenomenon`,`value`,`timestamp`) VALUES (" + str(PHENOMENON_TYPE) + ","+ str(PERSON_ID) +","+ str(SYSTOLIC_ID) + "," + str(PHENOMENON) + ",'"+ str(row[1]) + "', '"+ str(row[0]) +"')"
			print sql
			executeSQL(sql)

			######################################
			# Create an Measurement for binding Quantity to it
			######################################
			sql = "INSERT INTO `Measurement_Facts` (`Phenomenon_type_idPhenomenon`,`Person_idPerson`,`Unit_idUnit`,`Phenomenon_idPhenomenon`,`value`,`timestamp`) VALUES (" + str(PHENOMENON_TYPE) + ","+ str(PERSON_ID) +","+ str(SYSTOLIC_ID) + "," + str(PHENOMENON) + ",'"+ str(row[2]) + "', '"+ str(row[0]) +"')"
			print sql
			executeSQL(sql)

	finally: 
		f.close()

#########################
# Heart Rate
#########################

#Create the phenomenon type
executeSQL("INSERT INTO `Phenomenon_type` (`name`) VALUES('heart_rate');")
PHENOMENON_TYPE = getLastId()

#Create Dummy phenomenon
executeSQL("INSERT INTO `Phenomenon` (`name`) VALUES('Too High');")
PHENOMENON = getLastId()

#Create units
executeSQL("INSERT INTO `Unit` (`name`) VALUES ('bpm')");
BPM_ID = getLastId()

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
			sql = "INSERT INTO `Measurement_Facts` (`Phenomenon_type_idPhenomenon`,`Person_idPerson`,`Unit_idUnit`,`Phenomenon_idPhenomenon`,`value`,`timestamp`) VALUES"
			sql = sql + "(" + str(PHENOMENON_TYPE) + ","+ str(PERSON_ID) +","+ str(BPM_ID) + ","+ str(PHENOMENON) +",'"+ str(row[1]) + "', '"+ str(row[0]) +"')"
			print sql
			executeSQL(sql)

	finally: 
		f.close()

#########################
# Temperature
#########################

#Create the phenomenon type
executeSQL("INSERT INTO `Phenomenon_type` (`name`) VALUES('Temperature');")
PHENOMENON_TYPE = getLastId()

#Create Dummy phenomenon
executeSQL("INSERT INTO `Phenomenon` (`name`) VALUES('Too High');")
PHENOMENON = getLastId()

#Create units
executeSQL("INSERT INTO `Unit` (`name`) VALUES ('celcius')");
BPM_ID = getLastId()

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
			sql = "INSERT INTO `Measurement_Facts` (`Phenomenon_type_idPhenomenon`,`Person_idPerson`,`Unit_idUnit`,`Phenomenon_idPhenomenon`,`value`,`timestamp`) VALUES"
			sql = sql + "(" + str(PHENOMENON_TYPE) + ","+ str(PERSON_ID) +","+ str(BPM_ID) + ","+ str(PHENOMENON) +",'"+ str(row[1]) + "', '"+ str(row[0]) +"')"
			print sql
			executeSQL(sql)

	finally: 
		f.close()