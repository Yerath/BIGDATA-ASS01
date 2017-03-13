use fowler;

SELECT *
	FROM Measurement 
    JOIN Phenomenon_Type
		ON Measurement.Phenomenon_Type_idPhenomenon_Type = Phenomenon_Type.idPhenomenon_Type
	WHERE Phenomenon_Type.type = "blood_pressure"
		AND Measurement.timestamp >= '2015/01/01' and Measurement.timestamp <= '2015/01/30'
    
INTO OUTFILE '/Users/yerath/tmp/1661152.1.fowler.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
;