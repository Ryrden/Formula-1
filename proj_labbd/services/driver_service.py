from ..database import DatabaseConnection as database
from .base_service import with_db_connection
from .base_service import with_transaction_db_connection

class DriverService:
    @staticmethod
    def _get_dto_driver(driver_id, driver_ref, code, name, nationality):
        return {
            "driver_id": driver_id,
            "driver_ref": driver_ref,
            "code": code,
            "name": name,
            "nationality": nationality
        }

    @staticmethod
    @with_db_connection
    def get_driver_by_id(cursor, driver_id):
        query = ("SELECT D.driverid, D.driverref, D.code, CONCAT(D.forename, ' ', D.surname) AS name, D.nationality FROM Driver D WHERE D.driverid = %s")
        params = (driver_id,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        return DriverService._get_dto_driver(*row)

    @staticmethod
    @with_db_connection
    def get_related_drivers_by_forename(cursor, forename, constructorid):
        query = """
        SELECT D.driverid, D.driverref, D.code, CONCAT(D.forename, ' ', D.surname) AS name, D.nationality FROM Driver D
        WHERE D.forename = %s
          AND D.driverid IN (
              SELECT driverid
              FROM Results R
              WHERE R.constructorid = %s
          );
        """
        params = (forename, constructorid)

        cursor.execute(query, params)
        rows = cursor.fetchall()

        drivers = []

        for row in rows:
            driver = DriverService._get_dto_driver(*row)
            drivers.append(driver)

        return drivers

    @staticmethod
    @with_db_connection
    def get_all_drivers(cursor):
        query = ("SELECT D.driverid, D.driverref, D.code, CONCAT(D.forename, ' ', D.surname) AS name, D.nationality FROM Driver D;")

        cursor.execute(query)
        rows = cursor.fetchall()

        drivers = []

        for row in rows:
            driver = DriverService._get_dto_driver(*row)
            drivers.append(driver)

        return drivers

    @staticmethod
    @with_db_connection
    def get_amount_drivers(cursor):
        query = ("SELECT COUNT(D.driverid) FROM Driver D;")

        cursor.execute(query)
        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]

    @staticmethod
    @with_db_connection
    def get_amount_wins(cursor, driver_id):
        query = ("SELECT COUNT(R.driverid) FROM Results R WHERE R.driverid = %s AND R.position = 1")
        params = (driver_id,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]

    @staticmethod
    @with_db_connection
    def get_first_and_last_ocurrences(cursor, driver_id):
        query = ("SELECT MIN(RA.year) AS oldest, MAX(RA.year) AS latest FROM Results RE JOIN Races RA ON RE.raceid = RA.raceid WHERE RE.driverid = %s;")
        params = (driver_id,)

        cursor.execute(query, params)
        row = cursor.fetchone()
        
        if row is None:
            return None

        oldest, latest = row

        ocurrences_data = {
            "oldest": oldest,
            "latest": latest
        }

        return ocurrences_data
    

    @staticmethod
    @with_transaction_db_connection
    def insert_driver(cursor, driverref, number, code, forename, surname, dob, nationality):
        query = """
            INSERT INTO driver (driverref, number, code, forename, surname, dob, nationality, url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
        params = (driverref, number, code, forename, surname, dob, nationality, "")

        cursor.execute(query, params)