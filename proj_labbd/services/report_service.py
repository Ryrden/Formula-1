from ..database import DatabaseConnection as database
from .base_service import with_db_connection


class ReportService:
    @staticmethod
    def _execute(query):
        db_connection = database()
        cursor = db_connection.cursor()
        cursor.execute(query)
        report = cursor.fetchall()
        return report

    @staticmethod
    def get_report(id, input):
        # query = f"SELECT * FROM report{id}(COALESCE({input}, NULL))"
        if input is None:
            query = f"SELECT * FROM report{id}()"
        else:
            query = f"SELECT * FROM report{id}('{input}')"
        return ReportService._execute(query)
