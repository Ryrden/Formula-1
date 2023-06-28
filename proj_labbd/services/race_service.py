from .base_service import with_db_connection


class RaceService:
    @staticmethod
    def _get_dto_race(race_id, year, rownd, circuit_id, name, date, time):
        """Get a"""
        return {
            "race_id": race_id,
            "year": year,
            "round": rownd,
            "circuit_id": circuit_id,
            "name": name,
            "date": date,
            "time": time,
        }

    @staticmethod
    @with_db_connection
    def get_races_by_id(cursor, race_id):
        """Get races by id from database"""
        query = "SELECT R.raceid, R.year, R.round, R.circuitid, R.name, R.date, R.time FROM Races R WHERE R.raceid = %s;"
        params = (race_id,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        return RaceService._get_dto_race(*row)

    @staticmethod
    @with_db_connection
    def get_all_races(cursor):
        """Get all races from database"""
        query = "SELECT R.raceid, R.year, R.round, R.circuitid, R.name, R.date, R.time FROM Races R;"

        cursor.execute(query)
        rows = cursor.fetchall()

        races = []

        for row in rows:
            race = RaceService._get_dto_race(*row)
            races.append(race)

        return races

    @staticmethod
    @with_db_connection
    def get_amount_races(cursor):
        """ "Get amount races from database"""
        query = "SELECT COUNT(R.raceid) FROM Races R;"

        cursor.execute(query)
        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]
