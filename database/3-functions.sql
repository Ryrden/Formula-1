-- ############# This function is executed every time the constructor table undergoes any change, replicating this modification in the user table ############# --
DROP FUNCTION IF EXISTS FC_Register_Constructor;
CREATE FUNCTION FC_Register_Constructor(c constructors) RETURNS void AS
$$
DECLARE
    user_exists bool;
BEGIN
    -- Check that's if user exists before insert
    SELECT EXISTS(SELECT source_id
                  FROM Users
                  WHERE source_id = c.constructorid
                    AND type = 'RACING_TEAM')
    INTO user_exists;

    IF user_exists THEN
        RAISE EXCEPTION 'The constructor "%" is already a registered user', c.constructorref;
    END IF;

    INSERT INTO Users (login, password, type, source_id)
    VALUES (CONCAT(c.constructorref, '_c'),
            md5(c.constructorref),
            'RACING_TEAM',
            c.constructorid);
END;
$$ LANGUAGE plpgsql;

-- ############# This function is executed every time the driver table undergoes any change, replicating this modification in the user table ############# --
DROP FUNCTION IF EXISTS FC_Register_Driver;
CREATE FUNCTION FC_Register_Driver(d driver) RETURNS void AS
$$
DECLARE
    user_exists bool;
BEGIN
    -- Check that's if user exists before insert
    SELECT EXISTS(SELECT source_id
                  FROM Users
                  WHERE source_id = d.driverid
                    AND type = 'DRIVER')
    INTO user_exists;

    IF user_exists THEN
        RAISE EXCEPTION 'The driver "%" is already a registered user', d.driverref;
    END IF;

    INSERT INTO Users (login, password, type, source_id)
    VALUES (CONCAT(d.driverref, '_d'),
            md5(d.driverref),
            'DRIVER',
            d.driverid);
END;
$$ LANGUAGE plpgsql;
-- ######################################################################################################## --

-- ############# Function for insert trigger in Constructor table ############# --
DROP FUNCTION IF EXISTS FC_Insert_Constructor;
CREATE FUNCTION FC_Insert_Constructor() RETURNS trigger AS
$$
BEGIN
    PERFORM FC_Register_Constructor(NEW);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- ############# Function for insert trigger in Driver table ############# --
DROP FUNCTION IF EXISTS FC_Insert_Driver;
CREATE FUNCTION FC_Insert_Driver() RETURNS trigger AS
$$
BEGIN
    PERFORM FC_Register_Driver(NEW);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
-- ######################################################################################################## --
