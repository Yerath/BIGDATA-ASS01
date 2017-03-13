#!/usr/bin/python
# coding=utf-8
import csv
import glob
import sys
import pymysql
import string
import re

print "Importing Snowflake"

HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = ''
DATABASE = 'snowflake'
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
		# FILL IN DATE
		birthdate = string.split(str(row[3]),"-")
		sql = "INSERT INTO `Birthdate` (`day`,`month`,`year`) VALUES ('" + birthdate[2]+ "','" + birthdate[1]+ "','" + birthdate[0]+ "')";
		print(sql)
		executeSQL(sql)
		BIRTHDATE_ID = getLastId()

		sql = "INSERT INTO `Person` (`name`, `gender`, `studentnr`, `Birthdate_idBirthdate`) VALUES ('" + str(row[1]) + "', " + str(row[2]) + ", " + str(row[4]) + ", " + str(BIRTHDATE_ID) + ");"
		print(sql)
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
			print(sql)
			executeSQL(sql)

			######################################
			# Create an Measurement for binding Quantity to it
			######################################
			sql = "INSERT INTO `Measurement_Facts` (`Person_idPerson`, `value`, `timestamp`, `phenomenon`, `phenomenon_type`,`unit`) VALUES (" + str(PERSON_ID) + ", '" + str(row[2]) +"', '"+ str(row[0]) +"', '', 'blood_pressure', '"+ str(header[2]) +"');"
			print(sql)
			executeSQL(sql)

	finally: 
		f.close()

print "Filling Heart Rate"
#########################
# Heart Rate
#########################
for filename in glob.glob('../DATA/hr*'):

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
			print(sql)
			executeSQL(sql)

	finally: 
		f.close()

print "Filling Temperature"
#########################
# Temperature
#########################

for filename in glob.glob('../DATA/temp*'):

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
			print(sql)
			executeSQL(sql)

	finally: 
		f.close()