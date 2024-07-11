from src.models.repositories.participants_repository import ParticipantsRepository


class ParticipantConfirmer:
    def __init__(self, participant_repository: ParticipantsRepository) -> None:
        self.__participant_repository = participant_repository

    def participant_confirm(self, participant_id) -> dict:
        try:
            self.__participant_repository.update_participants_status(participant_id)
            return {"body": None, "status_code": 204}
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status_code": 400,
            }
