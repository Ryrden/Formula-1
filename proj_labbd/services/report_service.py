from .base_service import with_db_connection


class ReportService:
    @staticmethod
    @with_db_connection
    def _execute(cursor, query):
        cursor.execute(query)
        report = cursor.fetchall()
        return report

    @staticmethod
    def get_report(id, input):
        if input is None:
            query = f"SELECT * FROM report{id}()"
        else:
            query = f"SELECT * FROM report{id}('{input}')"
        return ReportService._execute(query)
