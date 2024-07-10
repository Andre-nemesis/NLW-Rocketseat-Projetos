from .emails_to_invite_repository import EmailsToInviteRepository
import pytest
from src.models.settings.db_connection_handler import db_connection_handler
import uuid

db_connection_handler.connect()

trip_id = "2e134181-0a43-47d4-a106-455612a9c4c4"


@pytest.mark.skip(reason="interacao com o banco")
def test_registry_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_reposirory = EmailsToInviteRepository(conn)

    emails_trips_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "seujorge@email.com",
    }

    emails_to_invite_reposirory.resgistry_email(emails_trips_infos)


@pytest.mark.skip(reason="interacao com o banco")
def test_find_email_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_reposirory = EmailsToInviteRepository(conn)
    emails = emails_to_invite_reposirory.find_email_from_trip(trip_id)

    print(emails)
