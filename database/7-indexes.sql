BEGIN;

-- Relatório 2
DROP INDEX IF EXISTS IDX_type_isocountry_airports;
CREATE INDEX IDX_type_isocountry_airports ON Airports (type, isocountry);

-- Relatório 3
DROP INDEX IF EXISTS IDX_constructorid_results;
CREATE INDEX IDX_constructorid_results ON Results (constructorid);

-- Relatório 5
DROP INDEX IF EXISTS IDX_driverid_results;
CREATE INDEX IDX_driverid_results ON Results (driverid);

COMMIT;