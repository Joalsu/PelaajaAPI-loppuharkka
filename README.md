# PelaajaAPI

## Pelaajan edistymisen seurantaan API. SAMK 2023 Backend-ohjelmointi lopputyö

### Toteutettu käyttäen FastAPI framework:kia ja Python:ia.

- Seurattavat eventit, tietyn kentän aloittamiseen ja tietyn kentän läpäisyyn.
- Voidaan kysellä pelaajien/pelaajan: nimet, id:t, tiedot, eventit.
- Voidaan kysellä myös koko "järjestelmässä": Kaikki eventit ja tietyn tyyppiset eventit.
- Uusien pelaajien ja eventtetien luonti ja näiden kutsuminen mistä tahansa lähteestä (originista)

#### Käyttö ja asennus

Varmista, että ladattu tiedostokansio on vain pelkkä yksi kansio, eikä
PelaajaAPI kansio, jonka sisällä toinen PelaajaAPI kansio.

-> Tämä siksi, että tiedostopolku viittaukset toimii oikein.

Avaa kansio Visual Studio Code:lla ja avaa Command Palette (Ctrl+Shift+P) oletus Windows:issa.
Etsi Venv (Virtuaali ympäristö) ja valtise ehdotettu asennettu Python versio polusta.

Tämän jälkeen:

1. pip install fastapi
2. pip install "uvicorn[standard]"
3. cd app
4. uvicorn main:app --reload
5. Uvicorn runnig on ... -> /docs
