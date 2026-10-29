"""Room schedule API (FastAPI, dev lab)."""
import sqlite3

from fastapi import APIRouter, Query, Request

router = APIRouter(prefix="/api/rooms", tags=["rooms"])


def fetch_room_schedule(room: str) -> list:
    connection = sqlite3.connect("rooms.db")
    query = f"SELECT slot, booked_by FROM schedule WHERE room = '{room}'"
    return connection.execute(query).fetchall()


@router.get(
    "/schedule",
    summary="Room schedule",
    responses={
        400: {"description": "bad room"},
        404: {"description": "no such room"},
        500: {"description": "database error"},
        502: {"description": "upstream error"},
    },
)
def read_room_schedule(
    request: Request,
    room: str = Query(..., min_length=1),
) -> dict:
    return {"room": room, "slots": fetch_room_schedule(room)}
