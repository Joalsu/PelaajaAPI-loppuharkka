from typing import List
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class EventIn(BaseModel):
    id: int
    type: str
    detail: str
    timestamp: str


class EventInCreate(BaseModel):
    type: str
    detail: str


class EventDb(EventIn):
    player_id: int


class PlayerInCreate(BaseModel):
    name: str


class PlayerIn(BaseModel):
    id: int
    name: str


class PlayerDb(PlayerIn):
    events: List[EventDb] = []


types = ['level_started', 'level_solved']
details = ['level_1212_001', 'level_1333_034']


events = [
    {'id': 1, 'type': types[(0)], 'detail': 'level_1212_001',
        'timestamp': datetime.now().strftime('%Y-%m-%d, %H:%M:%S'), 'player_id': 1},

    {'id': 2, 'type': types[(1)], 'detail': 'level_1333_034',
     'timestamp': datetime.now().strftime('%Y-%m-%d, %H:%M:%S'), 'player_id': 2}
]


players = [
    {'id': 1, 'name': 'Reijo', 'events': [events[0]]},
    {'id': 2, 'name': 'Veijo', 'events': [events[1]]}
]


# Palauttaa kaikkien pelaajien nimet ja id:t.
# Jos ei pelaajia, palauttaa tyhjän listan.
@app.get('/players', response_model=list[PlayerIn])
def get_players():
    return players


# Palauttaa tietyn pelaajan kaikki tiedot id:n perusteella.
# Jos kysellään tuntematonta pelaajaa, palautuu statuskoodi 404.
@app.get('/players/{id}', response_model=PlayerDb)
def get_player(id: int):
    index = -1
    for i, p in enumerate(players):
        if p['id'] == id:
            index = i
            break
    if index == -1:
        raise HTTPException(detail="Player not found", status_code=404)
    return players[index]


# Palauttaa kaikki eventit
# Jos ei eventtejä, tai ehdot eivät toteudu palauttaa tyhjän listan
# Jos kysellään tuntematonta eventtityyppiä, palautuu Bad Request 400
# type -kyselyparametrille tehdyt vastaavat eventit palutetaan
@app.get('/events', response_model=list[EventDb])
def get_events(type: str = None):
    if type is not None and type not in types:
        raise HTTPException(status_code=400, detail="Invalid event type")

    if type is None:
        return events

    filtered_events = [event for event in events if event['type'] == type]
    return filtered_events


# Palauttaa kysytyn pelaajan kaikki eventit tai kysytyn eventti tyypin
@app.get('/players/{id}/events', response_model=list[EventDb])
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


# Post uuden pelaajan luomiseen
# Jos request 'name' valuen annettu arvo ei ole vain aakkosia nostetaan virhe
@app.post('/players', status_code=status.HTTP_201_CREATED, response_model=PlayerIn)
def create_player(player_in: PlayerInCreate):
    if not player_in.name.isalpha():
        raise HTTPException(
            detail='Request contains invalid data', status_code=422)
    new_id = len(players) + 1
    player = PlayerDb(id=new_id, name=player_in.name)
    players.append(player.dict())
    return player


# Post uuden eventin luomiseen pelaajalle
@app.post('/players/{id}/events', status_code=status.HTTP_201_CREATED, response_model=EventDb)
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
