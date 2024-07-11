from src.models.repositories.trips_repository import TripsRepository


class TripConfirmer:
    def __init__(self, trip_repository: TripsRepository) -> None:
        self.__trip_repository = trip_repository

    def confirm(self, trip_id) -> dict:
        try:
            self.__trip_repository.update_trip_status(trip_id)
            return {"body": None, "status_code": 204}
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status_code": 400,
            }
