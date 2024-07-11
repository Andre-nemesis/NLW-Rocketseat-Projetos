from src.models.repositories.links_repository import LinksRepository


class LinkFinder:
    def __init__(self, links_repository: LinksRepository) -> None:
        self.__link_repository = links_repository

    def find(self, trip_id) -> dict:
        try:
            links = self.__link_repository.find_links_from_trip(trip_id)
            formatted_link = []

            for link in links:
                formatted_link.append({"id": link[0], "url": link[2], "url": link[3]})

            return {"body": {"formatted_links": formatted_link}, "status_code": 200}

        except Exception as e:
            return {
                "body": {"error": "Bad request", "message": str(e)},
                "status_code": 400,
            }
