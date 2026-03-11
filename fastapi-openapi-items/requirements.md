# Vaatimusmäärittely: FastAPI Items API

## 1. Tavoite
Tavoitteena on toteuttaa kevyt, tuotantoon laajennettava Python 3.11+ -pohjainen FastAPI-palvelu, joka tarjoaa OpenAPI-dokumentaation automaattisesti ja esimerkkidomainin `items`.

## 2. Laajuus
Sisältyy:
- REST-rajapinta domainille `items`
- Health-check endpoint
- In-memory tallennus
- Pydantic v2 -mallit request/response-rakenteille
- Testit, linttaus ja tyyppitarkistus
- Docker-ajettavuus

Ei sisälly tässä vaiheessa:
- Tietokanta
- Autentikointi/autorisointi
- Ulkoiset integraatiot

## 3. User Storyt
- Kehittäjänä haluan käynnistää API:n yhdellä komennolla, jotta voin aloittaa kehityksen nopeasti.
- API-kuluttajana haluan luoda ja hakea itemeitä, jotta voin tallentaa ja lukea perustietoa.
- Kehittäjänä haluan OpenAPI-kuvauksen automaattisesti, jotta endpointit ovat helposti löydettävissä ja testattavissa.

## 4. Acceptance Criteria (Given/When/Then)

### 4.1 Health check
Given palvelu on käynnissä  
When teen GET-pyynnön `/api/health`  
Then saan vastauksen `200 OK` ja rungon `{ "status": "ok" }`.

### 4.2 Itemin luonti
Given palvelu on käynnissä  
When teen POST-pyynnön `/api/items` validilla payloadilla  
Then saan vastauksen `201 Created` ja luodun itemin yksilöllisellä `id`:llä.

### 4.3 Itemin haku
Given item on olemassa  
When teen GET-pyynnön `/api/items/{item_id}`  
Then saan vastauksen `200 OK` ja itemin tiedot.

Given itemiä ei ole olemassa  
When teen GET-pyynnön `/api/items/{item_id}`  
Then saan vastauksen `404 Not Found` ja virheviestin.

### 4.4 Item-listaus
Given järjestelmässä on itemeitä  
When teen GET-pyynnön `/api/items`  
Then saan vastauksen `200 OK` ja listan itemeistä.

## 5. API-endpointit
- `GET /api/health`
- `GET /api/items`
- `POST /api/items`
- `GET /api/items/{item_id}`
- `GET /openapi.json`
- `GET /docs`
- `GET /redoc`

## 6. Tietomallit

### 6.1 ItemCreate (request)
- `name: str` (pakollinen)
- `description: str | null` (valinnainen)

### 6.2 Item (response)
- `id: int`
- `name: str`
- `description: str | null`

## 7. Ei-toiminnalliset vaatimukset
- Python 3.11+
- FastAPI + Uvicorn
- Pydantic v2 + pydantic-settings
- Testit pytestillä
- Linttaus ruffilla
- Typetys mypyllä
- Selkeä kerrosrakenne (`api`, `services`, `models`, `core`)

## 8. Avoimet jatkokehityskohteet
- In-memory tallennuksen korvaaminen tietokannalla
- Autentikointi (esim. JWT/OAuth2)
- Versionhallittu API (esim. `/api/v1`)
- Auditointi, lokitus ja metriikat
- Integraatiot ulkoisiin palveluihin
