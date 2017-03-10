use starschema;

SELECT *
	FROM Measurement_Facts
	JOIN Phenomenon_type
		ON Measurement_Facts.Phenomenon_type_idPhenomenon = Phenomenon_type.idPhenomenon
	WHERE Phenomenon_Type.name = "blood_pressure"
		AND Measurement_Facts.timestamp >= '2015/01/01' and Measurement_Facts.timestamp <= '2015/01/30'
