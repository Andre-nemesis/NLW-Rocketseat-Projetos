import uuid
from src.models.repositories.activities_repository import ActivitiesRepository


class ActivityCreator:
    def __init__(
        self,
        activity_repository: ActivitiesRepository,
    ) -> None:
        self.__activity_repository = activity_repository

    def create(self, body, trip_id) -> dict:
        try:
            activity_id = str(uuid.uuid4())

            activitys_infos = {
                "id": activity_id,
                "trip_id": trip_id,
                "title": body["title"],
                "occurs_at": body["occurs_at"],
            }
            self.__activity_repository.registry_activity(activitys_infos)
            return {"body": {"activity_id": activity_id}, "status_code": 201}
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status_code": 400,
            }
