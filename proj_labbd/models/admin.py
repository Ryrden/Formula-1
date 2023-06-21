# from ..services.admin_service import AdminService
from ..services.driver_service import DriverService
# from ..services.racing_team_service import RacingTeamService
# from ..services.races_service import RacesService
# from ..services.seasons_service import SeasonsService

class Admin:
    @staticmethod
    def get_amount_drivers():
        return DriverService.get_amount_drivers()

    @staticmethod
    def get_amount_racing_team():
        return RacingTeamService.get_amount_racing_team()

    @staticmethod
    def get_amount_races():
        return RacesService.get_amount_races()

    @staticmethod
    def get_amount_seasons():
        return SeasonsService.get_amount_seasons()
