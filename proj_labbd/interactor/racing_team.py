from ..services.racing_team_service import RacingTeamService
from ..services.report_service import ReportService


class RacingTeam:
    @staticmethod
    def get_racing_team_by_id(racing_team_id):
        '''Get a racing team by id'''
        return RacingTeamService.get_racing_team_by_id(racing_team_id)

    @staticmethod
    def get_amount_wins(racing_team_name):
        '''Get the amount of wins of a racing team given a racing team name'''
        return RacingTeamService.get_amount_wins(racing_team_name)

    @staticmethod
    def get_diff_drivers(driver_id):
        '''Get the amount of different drivers that have driven for a racing team given a driver id'''
        return RacingTeamService.get_diff_drivers(driver_id)

    @staticmethod
    def get_first_and_last_ocurrences(racing_team_name):
        '''Get the first and last ocurrences of a racing team given a racing team name'''
        return RacingTeamService.get_first_and_last_ocurrences(racing_team_name)

    @staticmethod
    def get_report(id, input = None):
        '''Get a report given a report id'''
        return ReportService.get_report(id, input)
