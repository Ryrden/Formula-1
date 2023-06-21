from ..database import DatabaseConnection as database
from .base_service import with_db_connection

class RacesService:
    @staticmethod
    def _get_dto_race(race_id, year, rownd, circuit_id, name, date, time):
        return {
            "race_id": race_id,
            "year": year,
            "round": rownd,
            "circuit_id": circuit_id,
            "name": name,
            "date": date,
            "time": time
        }

    @staticmethod
    def get_racer_by_id(race_id):
        db_connection = database()
        cursor = db_connection.cursor()

        query = ("SELECT R.raceid, R.year, R.round, R.circuitid, R.name, R.date, R.time FROM Races R WHERE R.raceid = %s;")
        params = (race_id,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        return RacesService._get_dto_race(*row)

    @staticmethod
    def get_all_races():
        db_connection = database()
        cursor = db_connection.cursor()

        query = ("SELECT R.raceid, R.year, R.round, R.circuitid, R.name, R.date, R.time FROM Races R;")

        cursor.execute(query)
        rows = cursor.fetchall()

        races = []

        for row in rows:
            race = RacesService._get_dto_race(*row)
            races.append(race)

        return races

    @staticmethod
    def get_amount_races():
        db_connection = database()
        cursor = db_connection.cursor()

        query = ("SELECT COUNT(R.raceid) FROM Races R;")

        cursor.execute(query)
        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]