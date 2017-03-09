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
		cursor.execute("SELECT last_insert_id()")
	connection.commit();
	return cursor.fetchone()['last_insert_id()']