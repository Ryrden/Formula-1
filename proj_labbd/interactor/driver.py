from ..services.driver_service import DriverService
from ..services.report_service import ReportService


class Driver:
    @staticmethod
    def get_driver_by_id(driver_id):
        '''Returns a driver by id'''
        return DriverService.get_driver_by_id(driver_id)

    @staticmethod
    def get_amount_wins(driver_id):
        '''Returns the amount of wins of a driver given his id'''
        return DriverService.get_amount_wins(driver_id)

    @staticmethod
    def get_first_and_last_ocurrences(driver_id):
        '''Returns the first and last ocurrences of a driver given his id'''
        return DriverService.get_first_and_last_ocurrences(driver_id)

    @staticmethod
    def get_related_drivers_by_forename(forename, constructorid):
        '''Returns the drivers related to a driver given his forename and constructorid'''
        return DriverService.get_related_drivers_by_forename(forename, constructorid)

    @staticmethod
    def get_report(id, input = None):
        '''Returns a report of a driver given his id'''
        return ReportService.get_report(id, input)
