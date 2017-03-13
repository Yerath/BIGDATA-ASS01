use fowler; 

SELECT 
	Person.idPerson,
	Person.name,
    (
		SELECT AVG( Quantity.value)
		FROM Measurement 
		JOIN Quantity ON Measurement.Quantity_idQuanitity = Quantity.idQuanitity
		JOIN Observation ON Measurement.Observation_idObservation = Observation.idObservation
		JOIN Phenomenon_Type ON Measurement.Phenomenon_Type_idPhenomenon_Type = Phenomenon_Type.idPhenomenon_Type
		WHERE Phenomenon_Type.type = "heart_rate"
		AND Observation.Person_idPerson = Person.idPerson
		AND Measurement.timestamp > '2015-01-23'
        AND Measurement.timestamp < '2015-01-24'
    ) as HeartRate_Average,
	(
		SELECT AVG( Quantity.value)
		FROM Measurement 
		JOIN Quantity ON Measurement.Quantity_idQuanitity = Quantity.idQuanitity
		JOIN Observation ON Measurement.Observation_idObservation = Observation.idObservation
		JOIN Phenomenon_Type ON Measurement.Phenomenon_Type_idPhenomenon_Type = Phenomenon_Type.idPhenomenon_Type
		WHERE Phenomenon_Type.type = "blood_pressure"
		AND Quantity.unit = "systolic"
		AND Observation.Person_idPerson = Person.idPerson
		AND Measurement.timestamp > '2015-01-23'
        AND Measurement.timestamp < '2015-01-24'
	) as Systolic_Average,
    (
		SELECT AVG( Quantity.value)
		FROM Measurement 
		JOIN Quantity ON Measurement.Quantity_idQuanitity = Quantity.idQuanitity
		JOIN Observation ON Measurement.Observation_idObservation = Observation.idObservation
		JOIN Phenomenon_Type ON Measurement.Phenomenon_Type_idPhenomenon_Type = Phenomenon_Type.idPhenomenon_Type
		WHERE Phenomenon_Type.type = "blood_pressure"
		AND Quantity.unit = "diastolic"
		AND Observation.Person_idPerson = Person.idPerson
        AND Measurement.timestamp > '2015-01-23'
        AND Measurement.timestamp < '2015-01-24'
	) as Diastolic_Average
FROM Measurement 
JOIN Quantity ON Measurement.Quantity_idQuanitity = Quantity.idQuanitity
JOIN Observation ON Measurement.Observation_idObservation = Observation.idObservation
JOIN Person ON Observation.Person_idPerson = Person.idPerson
GROUP BY
	Person.name, Person.idPerson
ORDER BY
	HeartRate_Average ASC

INTO OUTFILE '/Users/yerath/tmp/1661152.3.fowler.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
;
