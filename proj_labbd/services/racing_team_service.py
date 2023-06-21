from ..database import DatabaseConnection as database
from .base_service import with_db_connection

class RacingTeamService:
    @staticmethod
    def _get_dto_racing_team(constructor_id, constructor_ref, name, nationality):
        return {
            "constructor_id": constructor_id,
            "constructor_ref": constructor_ref,
            "name": name,
            "nationality": nationality
        }

    @staticmethod
    def get_racing_team_by_id(constructor_id):
        db_connection = database()
        cursor = db_connection.cursor()

        query = ("SELECT C.constructorid, C.constructorref, C.name, C.nationality FROM Constructors C WHERE C.constructorid = %s;")
        params = (constructor_id,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        return RacingTeamService._get_dto_racing_team(*row)

    @staticmethod
    def get_all_racing_teams():
        db_connection = database()
        cursor = db_connection.cursor()

        query = ("SELECT C.constructorid, C.constructorref, C.name, C.nationality FROM Constructors C;")

        cursor.execute(query)
        rows = cursor.fetchall()

        racing_teams = []

        for row in rows:
            racing_team = RacingTeamService._get_dto_racing_team(*row)
            racing_teams.append(racing_team)

        return racing_teams

    @staticmethod
    def get_amount_racing_team():
        db_connection = database()
        cursor = db_connection.cursor()

        query = ("SELECT COUNT(C.constructorid) FROM Constructors C;")

        cursor.execute(query)
        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]