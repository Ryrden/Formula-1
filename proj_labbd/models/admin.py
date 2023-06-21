from ..services.driver_service import DriverService
from ..services.racing_team_service import RacingTeamService
from ..services.race_service import RaceService
from ..services.season_service import SeasonService
from ..services.report_service import ReportService


class Admin:
    @staticmethod
    def get_amount_drivers():
        return DriverService.get_amount_drivers()

    @staticmethod
    def get_amount_racing_team():
        return RacingTeamService.get_amount_racing_team()

    @staticmethod
    def get_amount_races():
        return RaceService.get_amount_races()

    @staticmethod
    def get_amount_seasons():
        return SeasonService.get_amount_seasons()

    @staticmethod
    def get_report(id):
        return ReportService.get_report(id)
