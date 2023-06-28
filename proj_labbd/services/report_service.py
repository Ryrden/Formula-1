from .base_service import with_db_connection


class ReportService:
    @staticmethod
    @with_db_connection
    def _execute(cursor, query):
        """Executes a query and returns the result."""
        cursor.execute(query)
        report = cursor.fetchall()
        return report if report else None

    @staticmethod
    def get_report(id, input):
        """Returns the result of a report stored function in database."""
        if input is None:
            query = f"SELECT * FROM report{id}()"
        else:
            query = f"SELECT * FROM report{id}('{input}')"
        return ReportService._execute(query)
