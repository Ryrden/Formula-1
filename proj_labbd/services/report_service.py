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
        # query = f"SELECT * FROM report{id}(COALESCE({input}, NULL))"
        if input is None:
            query = f"SELECT * FROM report{id}()"
        else:
            input = type(input) is str and f"'{input}'" or input
            query = f"SELECT * FROM report{id}({input})"
        return ReportService._execute(query)
