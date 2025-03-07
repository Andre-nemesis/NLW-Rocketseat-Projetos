from src.models.repositories.participants_repository import ParticipantsRepository


class ParticipantFinder:
    def __init__(self, participant_repository: ParticipantsRepository) -> None:
        self.__participant_repository = participant_repository

    def find_participant_from_trip(self, trip_id: str) -> dict:
        try:
            participants = self.__participant_repository.find_participants_from_trip(
                trip_id
            )

            formatted_participants = []

            for participant in participants:
                formatted_participants.append(
                    {
                        "id": participant[0],
                        "name": participant[1],
                        "is_confirmed": participant[2],
                        "email": participant[3],
                    }
                )

            return {
                "body": {"participants_infos": formatted_participants},
                "status_code": 200,
            }

        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status_code": 400,
            }
