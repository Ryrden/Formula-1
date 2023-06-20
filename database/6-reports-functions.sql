BEGIN;

-- ADMIN

-- Relatório 1
DROP FUNCTION IF EXISTS report1();
CREATE OR REPLACE FUNCTION report1()
    RETURNS TABLE
            (
                status text,
                count  bigint
            )
AS
$$
BEGIN
    RETURN QUERY
        SELECT s.status, COUNT(*)
        FROM results r
                 JOIN status s USING (statusid)
        GROUP BY s.status, s.statusid
        ORDER BY s.statusid;
END;
$$ LANGUAGE plpgsql;

-- Relatório 2 -- Falta definir o Index (não analisei onde é melhor colocar)

CREATE EXTENSION IF NOT EXISTS Cube;
CREATE EXTENSION IF NOT EXISTS EarthDistance;

DROP FUNCTION IF EXISTS report2(text);
CREATE OR REPLACE FUNCTION report2(text)
    RETURNS TABLE
            (
                city         text,
                airport_iata char(3),
                airport_name text,
                airport_city text,
                distance     double precision,
                airport_type char(15)
            )
AS
$$
BEGIN
    RETURN QUERY
        SELECT a.city,
               a.iatacode,
               a.name,
               a.city,
               EARTH_DISTANCE(LL_TO_EARTH(a.latdeg, a.longdeg),
                              LL_TO_EARTH(g15k.lat, g15k.long)) AS distance,
               a.type
        FROM airports a
                 JOIN geocities15k g15k on g15k.name = $1
        WHERE a.type IN ('medium_airport', 'large_airport')
          AND a.isocountry = 'BR'
          AND EARTH_DISTANCE(LL_TO_EARTH(a.latdeg, a.longdeg),
                             LL_TO_EARTH(g15k.lat, g15k.long)) <= 100000
        ORDER BY a.city, distance;
END;
$$ LANGUAGE plpgsql;

-- Eu acho q esta certo mas n sei alguma cidade Brasileira para testar
select *
from report1();

-- ESCUDEIRA

COMMIT;