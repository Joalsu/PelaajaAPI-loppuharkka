from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


class PlayerIn(BaseModel):
    name: str


class PlayerDb(PlayerIn):
    id: int


players = [
    {'id': 1, 'name': 'Reijo'},
    {'id': 2, 'name': 'Veijo'}
]


# Palauttaa pelaajien nimet ja id:t.
# Jos ei pelaajia, palauttaa tyhjän listan.
@app.get('/players', response_model=list[PlayerDb])
def get_players():
    return players


# Post uuden pelaajan luomiseen
# Jos request 'name' valuen annettu arvo ei ole vain aakkosia nostetaan virhe
@app.post('/players', status_code=status.HTTP_201_CREATED, response_model=PlayerDb)
def create_player(player_in: PlayerIn):
    if not player_in.name.isalpha():
        raise HTTPException(
            detail='Request contains invalid data', status_code=422)
    new_id = len(players)
    player = PlayerDb(**player_in.dict(), id=new_id)
    players.append(player.dict())
    return player
