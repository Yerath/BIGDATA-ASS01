use snowflake;

SELECT
Person.name,
Person.idPerson,
timestamp,
    (SELECT AVG(value)
        FROM Measurement_Facts
        WHERE phenomenon_type = 'heart_rate'
        AND Measurement_Facts.timestamp > '2015-01-23'
        AND Measurement_Facts.timestamp < '2015-01-24'
        AND Measurement_Facts.Person_idPerson = Person.idPerson
    ) AS avgHartslag,
    (SELECT AVG(value)
        FROM Measurement_Facts
        WHERE unit = 'systolic'
        AND Measurement_Facts.timestamp > '2015-01-23'
        AND Measurement_Facts.timestamp < '2015-01-24'
        AND Measurement_Facts.Person_idPerson = Person.idPerson
    ) AS dystolic,
    (SELECT AVG(value)
        FROM Measurement_Facts
        WHERE unit = 'Diastolic'
        AND Measurement_Facts.timestamp > '2015-01-23'
        AND Measurement_Facts.timestamp < '2015-01-24'
        AND Measurement_Facts.Person_idPerson = Person.idPerson
    ) AS diastolic
FROM
    Measurement_Facts
JOIN
    Person
ON
    Measurement_Facts.Person_idPerson = Person.idPerson
where
    Measurement_Facts.timestamp > '2015-01-23'
    AND Measurement_Facts.timestamp < '2015-01-24'
    AND Measurement_Facts.phenomenon_type = 'blood_pressure'
GROUP BY
    Person.name,
    Person.idPerson
ORDER BY
    avgHartslag ASC
