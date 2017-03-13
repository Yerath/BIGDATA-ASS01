use fowler; 

SELECT count(idObservation), Person.name, Phenomenon_Type.type, DATE_FORMAT(Measurement.timestamp, '%Y %m %d')
FROM Observation
JOIN Person
	ON Observation.Person_idPerson = Person.idPerson
JOIN Measurement
	ON Measurement.Observation_idObservation = Observation.idObservation
JOIN Phenomenon_Type
	ON Phenomenon_Type.idPhenomenon_Type = Measurement.Phenomenon_Type_idPhenomenon_Type
GROUP BY DATE_FORMAT(Measurement.timestamp, '%Y %m %d'), Person.name, Phenomenon_Type.type

INTO OUTFILE '/Users/yerath/tmp/1661152.2.fowler.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
;