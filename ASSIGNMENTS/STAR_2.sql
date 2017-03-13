use starschema;

SELECT 
	count(idmeasurement_facts), 
	Person.name,
    phenomenon_type,
    DATE_FORMAT(timestamp, '%Y %m %d')
FROM
	Measurement_Facts
JOIN
	Person
ON
	Measurement_Facts.Person_idPerson = Person.idPerson
GROUP BY 
	DATE_FORMAT(timestamp, '%Y %m %d'), Person.name, phenomenon_type
    
INTO OUTFILE '/Users/yerath/tmp/1661152.2.star.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
;
    