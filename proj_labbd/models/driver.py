from ..services.driver_service import DriverService

class Driver:
    @staticmethod
    def get_driver_by_id(driver_id):
        return DriverService.get_driver_by_id(driver_id)

    @staticmethod
    def get_amount_wins(user):
        return DriverService.get_amount_wins(user)

    @staticmethod
    def get_occurrences(user):
        return DriverService.get_ocorrences(user)