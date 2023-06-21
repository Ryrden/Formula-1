from ..services.driver_service import DriverService

class Driver:
    @staticmethod
    def get_driver_by_id(driver_id):
        return DriverService.get_driver_by_id(driver_id)

    @staticmethod
    def get_amount_wins(driver_id):
        return DriverService.get_amount_wins(driver_id)

    @staticmethod
    def get_first_and_last_ocurrences(driver_id):
        return DriverService.get_first_and_last_ocurrences(driver_id)