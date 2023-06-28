from .base_service import with_db_connection


class SeasonService:
    @staticmethod
    def _get_dto_season(year, url):
        """Returns a dictionary with the season data"""
        return {"year": year, "url": url}

    @staticmethod
    @with_db_connection
    def get_season_by_year(cursor, year):
        """Returns a dictionary with the season data"""
        query = "SELECT S.year, S.url FROM Seasons S WHERE S.year = %s;"
        params = (year,)

        cursor.execute(query, params)
        row = cursor.fetchone()

        if row is None:
            return None

        return SeasonService._get_dto_season(*row)

    @staticmethod
    @with_db_connection
    def get_all_seasons(cursor):
        """Returns a list of dictionaries with the season data"""
        query = "SELECT S.year, S.url FROM Seasons S;"

        cursor.execute(query)
        rows = cursor.fetchall()

        seasons = []

        for row in rows:
            season = SeasonService._get_dto_season(*row)
            seasons.append(season)

        return seasons

    @staticmethod
    @with_db_connection
    def get_amount_seasons(cursor):
        """Returns the amount of seasons"""
        query = "SELECT COUNT(S.year) FROM Seasons S;"

        cursor.execute(query)
        row = cursor.fetchone()

        if row is None:
            return None

        return row[0]
