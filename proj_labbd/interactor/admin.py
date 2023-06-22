from ..services.driver_service import DriverService
from ..services.racing_team_service import RacingTeamService
from ..services.race_service import RaceService
from ..services.season_service import SeasonService
from ..services.report_service import ReportService


class Admin:
    @staticmethod
    def get_amount_drivers():
        '''Returns the amount of drivers in the database'''
        return DriverService.get_amount_drivers()

    @staticmethod
    def get_amount_racing_team():
        '''Returns the amount of racing teams in the database'''
        return RacingTeamService.get_amount_racing_team()

    @staticmethod
    def get_amount_races():
        '''Returns the amount of races the database'''
        return RaceService.get_amount_races()

    @staticmethod
    def get_amount_seasons():
        '''Returns the amount of seasons in the database'''
        return SeasonService.get_amount_seasons()

    @staticmethod
    def insert_racing_team(constructorid, constructorref, name, nationality, url):
        '''Inserts a racing team into the database'''
        return RacingTeamService.insert_racing_team(constructorid, constructorref, name, nationality, url)

    @staticmethod
    def insert_driver(driverid, driverref, number, code, forename, surname, dob, nationality, url):
        '''Inserts a driver into the database'''
        return DriverService.insert_driver(driverid, driverref, number, code, forename, surname, dob, nationality, url)

    @staticmethod
    def get_report(id, input = None):
        '''Returns a report'''
        return ReportService.get_report(id, input)
