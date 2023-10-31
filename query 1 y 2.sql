SELECT P.full_name, COUNT(C.id_person) AS appearance_count
FROM Casting AS C
JOIN Person AS P ON C.id_person = P.id_person
JOIN Shows AS S ON C.id_show = S.id_show
JOIN Platforms AS PL ON S.id_platform = PL.id_platform
WHERE PL.platform_name = 'Netflix'
AND C.id_role = 2 -- 2 representa el rol de actor
GROUP BY P.full_name
ORDER BY appearance_count DESC
LIMIT 1;



SELECT P.full_name, COUNT(C.id_person) AS appearance_count
FROM Casting AS C
JOIN Person AS P ON C.id_person = P.id_person
JOIN Shows AS S ON C.id_show = S.id_show
WHERE EXTRACT(YEAR FROM S.date_added) = 2015 --aca debe cambiar por el año que desee
GROUP BY P.full_name
ORDER BY appearance_count DESC
LIMIT 10;





