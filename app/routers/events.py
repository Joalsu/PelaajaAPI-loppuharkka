from routers.players import get_player
from database.models import EventDb, EventInCreate
from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from database.database import types, events, details


router = APIRouter(prefix='/events', tags=['events'])


# Palauttaa kysytyn pelaajan kaikki eventit tai kysytyn eventti tyypin
@router.get('/players/{id}/events', response_model=list[EventDb])
def get_events(id: int, type: str = None):
    if type is not None and type not in types:
        raise HTTPException(status_code=400, detail="Invalid event type")

    player = get_player(id)
    player_events = [dict(event) for event in player['events']]

    if type:
        filtered_events = [
            event for event in player_events if event['type'] == type]
    else:
        filtered_events = player_events

    return filtered_events


# Post uuden eventin luomiseen pelaajalle
@router.post('/players/{id}/events', status_code=status.HTTP_201_CREATED, response_model=EventDb)
def create_events(id: int, event_in: EventInCreate):

    # Tarkistetaan löytyykö pelaaja
    player = get_player(id)

    # Tarkistetaan onko eventti tyyppi oikea
    if event_in.type not in types:
        raise HTTPException(status_code=400, detail="Invalid event type")

    # Tarkistetaan onko annettu virheellistä dataa
    if event_in.detail not in details:
        raise HTTPException(
            status_code=422, detail="Request contains invalid data")

    # Luodaan uusi eventti
    new_id = len(events) + 1
    event = EventDb(id=new_id, type=event_in.type, detail=event_in.detail,
                    timestamp=datetime.now().strftime('%Y-%m-%d, %H:%M:%S'), player_id=id)
    events.append(event.dict())

    # Lisätään event pelaajalle
    player['events'].append(event)

    return event


# Palauttaa kaikki eventit
# Jos ei eventtejä, tai ehdot eivät toteudu palauttaa tyhjän listan
# Jos kysellään tuntematonta eventtityyppiä, palautuu Bad Request 400
# type -kyselyparametrille tehdyt vastaavat eventit palutetaan
@router.get('/events', response_model=list[EventDb])
def get_events(type: str = None):
    if type is not None and type not in types:
        raise HTTPException(status_code=400, detail="Invalid event type")

    if type is None:
        return events

    filtered_events = [event for event in events if event['type'] == type]
    return filtered_events
