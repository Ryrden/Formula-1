from ..services.racing_team_service import RacingTeamService
from ..services.report_service import ReportService


class RacingTeam:
    @staticmethod
    def get_racing_team_by_id(racing_team_id):
        return RacingTeamService.get_racing_team_by_id(racing_team_id)

    @staticmethod
    def get_amount_wins(racing_team_name):
        return RacingTeamService.get_amount_wins(racing_team_name)

    @staticmethod
    def get_diff_drivers(driver_id):
        return RacingTeamService.get_diff_drivers(driver_id)

    @staticmethod
    def get_first_and_last_ocurrences(racing_team_name):
        return RacingTeamService.get_first_and_last_ocurrences(racing_team_name)

    @staticmethod
    def get_report(id, input = None):
        return ReportService.get_report(id, input)
