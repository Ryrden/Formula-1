from ..database import DatabaseConnection as database
from .base_service import with_db_connection

class SeasonService:
    @staticmethod   
    def _get_dto_season(year, url):
        return {
            "year": year,
            "url": url
        }

    @staticmethod
    def get_season_by_year(year):
        db_connection = database()
        cursor = db_connection.cursor()

        query = ("SELECT S.year, S.url FROM Seasons S WHERE S.year = %s;")
        params = (year,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        return SeasonService._get_dto_season(*row)

    @staticmethod
    def get_all_seasons():
        db_connection = database()
        cursor = db_connection.cursor()

        query = ("SELECT S.year, S.url FROM Seasons S;")

        cursor.execute(query)
        rows = cursor.fetchall()

        seasons = []

        for row in rows:
            season = SeasonService._get_dto_season(*row)
            seasons.append(season)

        return seasons

    @staticmethod
    def get_amount_seasons():
        db_connection = database()
        cursor = db_connection.cursor()

        query = ("SELECT COUNT(S.year) FROM Seasons S;")

        cursor.execute(query)
        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]