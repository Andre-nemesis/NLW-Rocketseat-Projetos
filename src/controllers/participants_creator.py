import uuid
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.participants_repository import ParticipantsRepository


class ParticipantCreator:
    def __init__(
        self,
        participant_repository: ParticipantsRepository,
        email_repository: EmailsToInviteRepository,
    ) -> None:
        self.__participant_repository = participant_repository
        self.__email_repository = email_repository

    def create(self, body, trip_id) -> dict:
        try:
            participant_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())

            emails_infos = {
                "id": email_id,
                "email": body["email"],
                "trip_id": trip_id,
            }

            participant_infos = {
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite_id": email_id,
                "name": body["name"],
            }

            self.__email_repository.resgistry_email(emails_infos)
            self.__participant_repository.registry_participant(participant_infos)

            return {"body": {"participant_id": participant_id}, "status_code": 201}

        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status_code": 400,
            }
