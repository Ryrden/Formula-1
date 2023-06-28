from .base_service import with_db_connection
from .base_service import with_transaction_db_connection


class RacingTeamService:
    @staticmethod
    def _get_dto_racing_team(constructor_id, constructor_ref, name, nationality):
        """Return a dictionary with the racing team data"""
        return {
            "constructor_id": constructor_id,
            "constructor_ref": constructor_ref,
            "name": name,
            "nationality": nationality,
        }

    @staticmethod
    @with_db_connection
    def get_racing_team_by_id(cursor, constructor_id):
        """Return a dictionary with the racing team data"""
        query = "SELECT C.constructorid, C.constructorref, C.name, C.nationality FROM Constructors C WHERE C.constructorid = %s;"
        params = (constructor_id,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        return RacingTeamService._get_dto_racing_team(*row)

    @staticmethod
    @with_db_connection
    def get_all_racing_teams(cursor):
        """Return a list of dictionaries with the racing team data"""
        query = "SELECT C.constructorid, C.constructorref, C.name, C.nationality FROM Constructors C;"

        cursor.execute(query)
        rows = cursor.fetchall()

        racing_teams = []

        for row in rows:
            racing_team = RacingTeamService._get_dto_racing_team(*row)
            racing_teams.append(racing_team)

        return racing_teams

    @staticmethod
    @with_db_connection
    def get_amount_racing_team(cursor):
        """Return the amount of racing teams"""
        query = "SELECT COUNT(C.constructorid) FROM Constructors C;"

        cursor.execute(query)
        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]

    @staticmethod
    @with_db_connection
    def get_amount_wins(cursor, constructor_id):
        """Return the amount of wins of a racing team"""
        query = "SELECT COUNT(R.resultid) FROM Results R WHERE R.constructorid = %s AND R.position = 1;"
        params = (constructor_id,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]

    @staticmethod
    @with_db_connection
    def get_diff_drivers(cursor, constructor_id):
        """Return the amount of different drivers of a racing team"""
        query = "SELECT COUNT(DISTINCT R.driverid) FROM Results R WHERE R.constructorid = %s;"
        params = (constructor_id,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]

    @staticmethod
    @with_db_connection
    def get_first_and_last_ocurrences(cursor, constructor_id):
        """Return the first and last ocurrences of a racing team"""
        query = "SELECT MIN(RA.year) AS oldest, MAX(RA.year) AS latest FROM Results RE JOIN Races RA ON RE.raceid = RA.raceid WHERE RE.constructorid = %s;"
        params = (constructor_id,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        oldest, latest = row

        ocurrences_data = {"oldest": oldest, "latest": latest}

        return ocurrences_data

    @staticmethod
    @with_transaction_db_connection
    def insert_racing_team(
        cursor, constructorid, constructorref, name, nationality, url
    ):
        """Insert a racing team into the database"""
        query = "INSERT INTO constructors (constructorid, constructorref, name, nationality, url) VALUES (%s, %s, %s, %s, %s);"
        params = (constructorid, constructorref, name, nationality, url)

        cursor.execute(query, params)
