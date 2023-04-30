# PelaajaAPI

## Pelaajan edistymisen seurantaan API. SAMK 2023 Backend-ohjelmointi lopputyö

### Toteutettu käyttäen FastAPI framework:kia, Python:ia ja relaatiotietokantana SQLite:ä

- Seurattavat eventit, tietyn kentän aloittamiseen ja tietyn kentän läpäisyyn.
- Voidaan kysellä pelaajien/pelaajan: nimet, id:t, tiedot, eventit.
- Voidaan kysellä myös koko "järjestelmässä": Kaikki eventit ja tietyn tyyppiset eventit.
- Uusien pelaajien ja eventtetien luonti ja näiden kutsuminen mistä tahansa lähteestä (originista)

#### Käyttö ja asennus

1. pip install fastapi
2. pip install "uvicorn[standard]"
3. cd app
4. uvicorn main:app --reload
5. Uvicorn runnig on ... -> /docs
