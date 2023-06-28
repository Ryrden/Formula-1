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

-- Relatório 2

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

-- ESCUDEIRA

-- Relatório 3

CREATE OR REPLACE FUNCTION report3(int)
    RETURNS TABLE
            (
                name text,
                wins bigint
            )
AS
$$
BEGIN
    RETURN QUERY
        SELECT CONCAT(d.forename, ' ', d.surname) AS name,
               COUNT(*)                           AS wins --Considerar Window Function
        FROM results r
                 JOIN driver d USING (driverid)
        WHERE constructorid = $1
          AND r.position = 1
        GROUP BY name
        ORDER BY wins DESC;
END;
$$ LANGUAGE plpgsql;

-- Relatório 4

CREATE OR REPLACE FUNCTION report4(int)
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
        WHERE r.constructorid = $1
        GROUP BY s.status, s.statusid
        ORDER BY s.statusid;
END;
$$ LANGUAGE plpgsql;

-- PILOTO

-- Relatório 5

CREATE OR REPLACE FUNCTION report5(int)
    RETURNS TABLE
            (
                wins bigint,
                year integer,
                race text
            )
AS
$$
BEGIN
    RETURN QUERY
        SELECT COUNT(*) AS wins, ra.year, ra.name
        FROM results rs
                 JOIN races ra USING (raceid)
        WHERE rs.driverid = $1
          AND rs.position = 1
        GROUP BY ROLLUP (ra.year, ra.name)
        ORDER BY ra.year DESC NULLS FIRST, ra.name NULLS FIRST; -- FIRST LINE = TOTAL WINS
END;
$$ LANGUAGE plpgsql;

-- Relatório 6

CREATE OR REPLACE FUNCTION report6(int)
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
        WHERE r.driverid = $1
        GROUP BY s.status, s.statusid
        ORDER BY s.statusid;
END;
$$ LANGUAGE plpgsql;

COMMIT;
