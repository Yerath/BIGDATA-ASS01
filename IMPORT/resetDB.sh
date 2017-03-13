#!/bin/bash
echo "Deleting the databases"
mysqladmin -u root -p drop fowler -f
mysqladmin -u root -p drop starschema -f
mysqladmin -u root -p drop snowflake -f

echo "Creating them again"
mysqladmin -u root -p create fowler
mysqladmin -u root -p create starschema
mysqladmin -u root -p create snowflake

echo "Filling Database"
mysql -u root -p fowler < ../SQL/FowlerObservation.sql 
mysql -u root -p starschema < ../SQL/StarSchema.sql 
mysql -u root -p snowflake < ../SQL/Snowflake.sql

python importFowler.py
python importSnowFlake.py
python importStarSchema.py 
