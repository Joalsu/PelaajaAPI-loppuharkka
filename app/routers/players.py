from fastapi import APIRouter, HTTPException, status
from database.models import PlayerDb, PlayerIn, PlayerInCreate
from database.database import players


router = APIRouter(prefix='/players', tags=['players'])


# Palauttaa kaikkien pelaajien nimet ja id:t.
# Jos ei pelaajia, palauttaa tyhjän listan.
@router.get('', response_model=list[PlayerIn])
def get_players():
    return players


# Palauttaa tietyn pelaajan kaikki tiedot id:n perusteella.
# Jos kysellään tuntematonta pelaajaa, palautuu statuskoodi 404.
@router.get('/{id}', response_model=PlayerDb)
def get_player(id: int):
    index = -1
    for i, p in enumerate(players):
        if p['id'] == id:
            index = i
            break
    if index == -1:
        raise HTTPException(detail="Player not found", status_code=404)
    return players[index]


# Post uuden pelaajan luomiseen
# Jos request 'name' valuen annettu arvo ei ole vain aakkosia nostetaan virhe
@router.post('', status_code=status.HTTP_201_CREATED, response_model=PlayerIn)
def create_player(player_in: PlayerInCreate):
    if not player_in.name.isalpha():
        raise HTTPException(
            detail='Request contains invalid data', status_code=422)
    new_id = len(players) + 1
    player = PlayerDb(id=new_id, name=player_in.name)
    players.append(player.dict())
    return player
