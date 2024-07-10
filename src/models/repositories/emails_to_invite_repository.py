from sqlite3 import Connection


class EmailsToInviteRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def resgistry_email(self, emails_infos: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO emails_to_invite
                    (id, trip_id, email)
                VALUES
                    (?,?,?)
            """,
            (
                emails_infos["id"],
                emails_infos["trip_id"],
                emails_infos["email"],
            ),
        )

        self.__conn.commit()

    def find_email_from_trip(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()

        cursor.execute(
            """
            SELECT * FROM emails_to_invite WHERE trip_id = ?
            """,
            (trip_id,),
        )

        trip = cursor.fetchall()
        return trip
