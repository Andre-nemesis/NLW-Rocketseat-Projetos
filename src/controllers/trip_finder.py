from src.models.repositories.trips_repository import TripsRepository


class TripFinder:
    def __init__(self, trip_reposiroty: TripsRepository):
        self.__trip_repository = trip_reposiroty

    def find_trip_details(self, trip_id) -> dict:
        try:
            trip = self.__trip_repository.find_trip_by_id(trip_id)

            if not trip:
                raise Exception(f"No trip found for this id: {trip_id}")
            return {
                "body": {
                    "trip": {
                        "id": trip[0],
                        "destination": trip[1],
                        "starts_at": trip[2],
                        "ends_at": trip[3],
                        "status": trip[6],
                    }
                },
                "status_code": 200,
            }
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status_code": 400,
            }
