from sqlite3 import Connection

# TODO: realizar testes


class ParticipantsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_participant(self, participant: dict) -> None:
        cursor = self.__conn.cursor()

        cursor.execute(
            """
            INSERT INTO participants
                (id, trip_id, emails_to_invite_id, name)
            VALUES
                (?, ?, ?, ?)
                        
            """,
            (
                participant["id"],
                participant["trip_id"],
                participant["emails_to_invite_id"],
                participant["name"],
            ),
        )
        self.__conn.commit()

    def find_participants_from_trip(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()

        cursor.execute(
            """
                SELECT p.id, p.name, p.is_confirmed, e.email
                    FROM participants as p
                    JOIN emails_to_invite as e ON e.id = p.emails_to_invite_id
                WHERE p.trip_id = ?
            """,
            [
                trip_id,
            ],
        )
        participants = cursor.fetchall()
        return participants

    def update_participants_status(self, participant_id: str) -> None:
        cursor = self.__conn.cursor()

        cursor.execute(
            """
                UPDATE participants 
                    SET is_confirmed = 1
                WHERE
                    id = ?
            """,
            (participant_id,),
        )

        self.__conn.commit()
