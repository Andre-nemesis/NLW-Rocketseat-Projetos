from sqlite3 import Connection

# TODO: realizar testes


class ActivitiesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_activity(self, activities_infos: dict) -> None:
        cursor = self.__conn.cursor()

        cursor.execute(
            """
            INSERT INTO activities 
                (id, trip_id, title, occurs_at)
            VALUES
                (?, ?, ?, ?)
                        
            """,
            (
                activities_infos["id"],
                activities_infos["trip_id"],
                activities_infos["title"],
                activities_infos["occurs_at"],
            ),
        )
        self.__conn.commit()

    def find_activitites_from_trip(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()

        cursor.execute(
            """
                SELECT * FROM activities WHERE trip_id = ?
            """,
            [
                trip_id,
            ],
        )
        activities = cursor.fetchall()
        return activities
