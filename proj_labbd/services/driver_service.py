from ..database import DatabaseConnection as database
from .base_service import with_db_connection

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
    def get_driver_by_id(driver_id):
        db_connection = database()
        cursor = db_connection.cursor()

        query = ("SELECT D.driverid, D.driverref, D.code, CONCAT(D.forename, ' ', D.surname) AS name, D.nationality FROM Driver D WHERE D.driverid = %s")
        params = (driver_id,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        return DriverService._get_dto_driver(*row)

    @staticmethod
    def get_all_drivers():
        db_connection = database()
        cursor = db_connection.cursor()

        query = ("SELECT D.driverid, D.driverref, D.code, CONCAT(D.forename, ' ', D.surname) AS name, D.nationality FROM Driver D;")

        cursor.execute(query)
        rows = cursor.fetchall()

        drivers = []

        for row in rows:
            driver = DriverService._get_dto_driver(*row)
            drivers.append(driver)

        return drivers

    @staticmethod
    def get_amount_drivers():
        db_connection = database()
        cursor = db_connection.cursor()

        query = ("SELECT COUNT(D.driverid) FROM Driver D;")

        cursor.execute(query)
        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]

    @staticmethod
    def get_amount_wins(driver_id):
        db_connection = database()
        cursor = db_connection.cursor()

        query = ("SELECT COUNT(R.driverid) FROM Results R WHERE R.driverid = %s AND R.position = 1")
        params = (driver_id,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]

    @staticmethod
    def get_first_and_last_ocurrences(driver_id):
        db_connection = database()
        cursor = db_connection.cursor()

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
    