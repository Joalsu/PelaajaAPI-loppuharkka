## Resurssit

#### Pelaajat

- id
- name
- events

name -kentän arvo ei ole uniikki, pelaajat tunnistetaan id :n perusteella. events on lista
pelaajan tapahtumia.

## Eventit

- id
- type
- detail
- player_id
- timestamp

Tunnetut eventtityypit "type" -kenttä:

- level_started
- level_solved

detail -tieto kertoo lisätietoja eventistä. Esimerkiksi level_started ja level_solved -
tapahtumissa se kertoo kentän nimen.

timestamp -kentän arvo on palvelimen aikaleima (päivämäärällä) tallennushetkellä.
player_id kertoo sen pelaajan id:n jolle tapahtuma kuuluu.

## Endpointit

#### -------GET:it-------

##### --- GET /players - palauttaa pelaajien nimet ja id:t ----

-> Statuskoodi 200
-> Jos ei pelaajia, palauttaa tyhjän listan.

id: 1,
name: " "

##### --- GET /players/{id} - palauttaa tietyn pelaajan kaikki tiedot ---

-> Statuskoodi 200
-> Jos kysellään tuntematonta pelaajaa, palautuu statuskoodi 404

id: 1,
name: " ",
events: [
id: 1,
type: " ",
detail: " ",
timestamp: " ",
player_id: 1
]

##### --- GET /players/{id}/events - palauttaa tietyn pelaajan kaikki eventit ---

Voidaan antaan kyselyparametri "type" , jonka kanssa suodatetaan vain tietyn tyypin
tapahtumat.
-> Statuskoodi 200.
-> Jos kysellään tuntematonta pelaajaa, palautuu statuskoodi 404
-> Jos tuntematon eventtityyppi, palautuu statuskoodi 400
-> Jos ei eventtejä, palautuu tyhjä lista.

id: 1,
type: " ",
detail: " ",
timestamp: " ",
player_id: 1

##### --- GET /events - palauttaa kaikki eventit ---

-> Statuskoodi 200
-> Jos ei eventtejä, palautuu tyhjä lista.
-> Jos kysellään tuntematonta eventtityyppiä, palautuu Bad Request 400

[
id: 1123,
type: " ",
detail: " ",
timestamp: " ",
player_id: 1

id: 1144,
type: " ",
detail: " ",
timestamp: " ",
player_id: 4
]

#### -------POST:it-------

##### --- POST /players - uuden pelaajan luomiseen ---

-> Onnistuessa palautuu statuskoodi 201
Paluuviestin sisältämän id -kentän arvo on uniikki jokaiselle luodulle resurssille.
-> Jos request sisältää virheellistä dataa, palautuu statuskoodi 422

name: " "

id: 3,
name: " "

##### --- POST /players/{id}/events - luo uuden eventin pelaajalle ---

-> Jos tuntematon pelaaja, palautuu statuskoodi 404
-> Jos tuntematon eventtityyppi, palautuu statuskoodi 400
-> Jos request sisältää virheellistä dataa, palautuu statuskoodi 422
-> Onnistuessa statuskoodina 201

type: " ",
detail: " "

id: 1123,
type: " ",
detail: " ",
timestamp: " ",
player_id: 1
