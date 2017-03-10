use snowflake;


SELECT *
	FROM Measurement_Facts
	JOIN Observation
		ON Measurement_Facts.Observation_idObservation = Observation.idObservation
	JOIN Phenomenon_Type
		ON Observation.Phenomenon_Type_idPhenomenon_Type = Phenomenon_Type.idPhenomenon_Type
	WHERE Phenomenon_Type.name = "blood_pressure"
		AND Measurement_Facts.timestamp >= '2015/01/01' and Measurement_Facts.timestamp <= '2015/01/30'