from src.models.repositories.links_repository import LinksRepository
import uuid


class LinkCreator:
    def __init__(self, links_repository: LinksRepository) -> None:
        self.__link_repository = links_repository

    def create_link(self, body, trip_id) -> dict:
        try:
            link_id = str(uuid.uuid4())

            link_infos = {
                "id": link_id,
                "link": body["url"],
                "title": body["title"],
                "trip_id": trip_id,
            }

            self.__link_repository.insert_link(link_infos)
            return {"body": {"linkId": link_id}, "status_code": 201}
        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status_code": 400,
            }
