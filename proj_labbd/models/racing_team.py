from ..services.racing_team_service import RacingTeamService

class RacingTeam:
    @staticmethod
    def get_racing_team_by_id(racing_team_id):
        return RacingTeamService.get_racing_team_by_id(racing_team_id)

    @staticmethod
    def get_amount_wins(racing_team_name):
        return RacingTeamService.get_amount_wins(racing_team_name)

    @staticmethod
    def get_amount_different_drivers(driver_id):
        return RacingTeamService.get_amount_different_drivers(driver_id)

    @staticmethod
    def get_occurrences(racing_team_name):
        return RacingTeamService.get_ocurrences(racing_team_name)