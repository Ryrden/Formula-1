BEGIN;

-- ############# Trigger for new records in Constructors table ############# --
CREATE OR REPLACE TRIGGER TG_Insert_Constructor
    BEFORE INSERT
    ON Constructors
    FOR EACH ROW
EXECUTE FUNCTION FC_Register_Constructor();

-- ############# Trigger for a updated records in Constructors table ############# --
CREATE OR REPLACE TRIGGER TG_Update_Constructor
    AFTER UPDATE
    ON Constructors
    FOR EACH ROW
EXECUTE FUNCTION FC_Register_Constructor();

-- ############# Trigger for new records in Drivers table ############# --
CREATE OR REPLACE TRIGGER TG_Insert_Driver
    BEFORE INSERT
    ON Driver
    FOR EACH ROW
EXECUTE FUNCTION FC_Register_Driver();

-- ############# Trigger for a updated records in Drivers table ############# --
CREATE OR REPLACE TRIGGER TG_Update_Driver
    AFTER UPDATE
    ON Driver
    FOR EACH ROW
EXECUTE FUNCTION FC_Register_Driver();

COMMIT;
