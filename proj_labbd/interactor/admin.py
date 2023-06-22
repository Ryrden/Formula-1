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
    def insert_racing_team(constructorref, name, nationality, url):
        return RacingTeamService.insert_racing_team(constructorref, name, nationality, url)

    @staticmethod
    def insert_driver(driverref, number, code, forename, surname, dob, nationality):
        return DriverService.insert_driver(driverref, number, code, forename, surname, dob, nationality)

    @staticmethod
    def get_report(id, input = None):
        return ReportService.get_report(id, input)
