from typing import Dict
import uuid
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.drivers.email_sender import send_email


class TripCreator:
    def __init__(
        self,
        trip_repository: TripsRepository,
        emails_repository: EmailsToInviteRepository,
    ) -> None:
        self.__trip_repository = trip_repository
        self.__emails_repository = emails_repository

    def create(self, body) -> Dict:
        try:
            emails = body.get("emails_to_invite")

            trip_id = str(uuid.uuid4())

            trip_infos = {**body, "id": trip_id}

            self.__trip_repository.create_trip(trip_infos)

            if emails:
                for email in emails:
                    self.__emails_repository.resgistry_email(
                        {"email": email, "trip_id": trip_id, "id": str(uuid.uuid4())}
                    )

            send_email(
                [body["owner_email"]], f"http://localhost:3000/trips/{trip_id}/confirm"
            )

            return {"body": {"id": trip_id}, "status_code": 201}

        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status_code": 400,
            }
