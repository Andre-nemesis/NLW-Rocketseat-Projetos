from .links_repository import LinksRepository
import pytest
from src.models.settings.db_connection_handler import db_connection_handler
import uuid

db_connection_handler.connect()

trip_id = "2e134181-0a43-47d4-a106-455612a9c4c4"


@pytest.mark.skip(reason="interação com o banco")
def test_insert_link():
    conn = db_connection_handler.get_connection()
    links_reposirory = LinksRepository(conn)

    links_trips_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "youtube.com/watch=384534",
        "title": "local de viagem",
    }

    links_reposirory.insert_link(links_trips_infos)


@pytest.mark.skip(reason="interação com o banco")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_reposirory = LinksRepository(conn)
    links = links_reposirory.find_links_from_trip(trip_id)

    assert isinstance(links, list)
    assert isinstance(links[0], tuple)

    print(links)
