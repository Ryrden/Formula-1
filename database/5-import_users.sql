-- ############# This SQL query allows to create a Admin User in the Users table ############# --
INSERT INTO Users (login, password, type, source_id)
VALUES ('admin', 'admin', 'ADMIN', 0);

-- ############# This SQL query allows you to migrate all existing data from the Constructor table to the Users table ############# --
INSERT INTO Users (login, password, type, source_id)
SELECT CONCAT(C.constructorref, '_c'), MD5(C.constructorref), 'RACING_TEAM', C.constructorid
FROM Constructors C;

-- ############# This SQL query allows you to migrate all existing data from the Driver table to the Users table ############# --
INSERT INTO Users (login, password, type, source_id)
SELECT CONCAT(D.driverref, '_d'), MD5(D.driverref), 'DRIVER', D.driverid
FROM Driver D;
