-- ############# This function is executed every time the constructor table undergoes any change, replicating this modification in the user table ############# --
CREATE OR REPLACE FUNCTION FC_Register_Constructor() RETURNS TRIGGER AS
$$
DECLARE
    user_exists bool;
BEGIN
    CASE TG_OP
        WHEN 'INSERT' THEN -- Check that's if user exists before insert
        SELECT EXISTS(SELECT source_id
                      FROM Users
                      WHERE source_id = NEW.constructorid
                        AND type = 'RACING_TEAM')
        INTO user_exists;

        IF user_exists THEN
            RAISE EXCEPTION 'The constructor "%" is already a registered user', NEW.constructorref;
        END IF;

        INSERT INTO Users (login, password, type, source_id)
        VALUES (CONCAT(NEW.constructorref, '_c'),
                md5(NEW.constructorref),
                'RACING_TEAM',
                NEW.constructorid);

        WHEN 'UPDATE' THEN UPDATE Users
                           SET login    = CONCAT(NEW.constructorref, '_c'),
                               password = md5(NEW.constructorref),
                               type     = 'RACING_TEAM'
                           WHERE source_id = NEW.constructorid
                             AND type = 'RACING_TEAM';

        END CASE;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
COMMIT;

-- ############# This function is executed every time the driver table undergoes any change, replicating this modification in the user table ############# --
CREATE OR REPLACE FUNCTION FC_Register_Driver() RETURNS TRIGGER AS
$$
DECLARE
    user_exists bool;
BEGIN
    CASE TG_OP
        WHEN 'INSERT' THEN -- Check that's if user exists before INSERT
        SELECT EXISTS(SELECT source_id
                      FROM Users
                      WHERE source_id = NEW.driverid
                        AND type = 'DRIVER')
        INTO user_exists;

        IF user_exists THEN
            RAISE EXCEPTION 'The driver "%" is already a registered user', NEW.driverref;
        END IF;

        INSERT INTO Users (login, password, type, source_id)
        VALUES (CONCAT(NEW.driverref, '_d'),
                md5(NEW.driverref),
                'DRIVER',
                NEW.driverid);

        WHEN 'UPDATE' THEN UPDATE Users
                           SET login    = CONCAT(NEW.driverref, '_d'),
                               password = md5(NEW.driverref),
                               type     = 'DRIVER'
                           WHERE source_id = NEW.driverid
                             AND type = 'DRIVER';

        END CASE;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
COMMIT;
-- ######################################################################################################## --
