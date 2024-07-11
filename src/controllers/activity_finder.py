from src.models.repositories.activities_repository import ActivitiesRepository


class ActivityFinder:
    def __init__(self, activity_repository: ActivitiesRepository) -> None:
        self.__activity_repository = activity_repository

    def find_activity_from_trip(self, trip_id: str) -> dict:
        try:
            activities = self.__activity_repository.find_activitites_from_trip(trip_id)

            activities_formatted = []
            for activity in activities:
                activities_formatted.append(
                    {"id": activity[0], "title": activity[1], "occurs_at": activity[3]}
                )

            return {
                "body": {"activities_infos": activities_formatted},
                "status_code": 200,
            }

        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status_code": 400,
            }
