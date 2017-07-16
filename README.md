Ubicajeros API
===========

[![Lintly](https://lintly.com/gh/ivansabik/ubicajeros-api/badge.svg)](https://lintly.com/gh/ivansabik/ubicajeros-api/)

HTTP API for getting ATMs (Cajeros) available in Mexico. If gets the information from calls to the ubicajeros app from Banco de Mexico (BANXICO).

Dependencies:
- flask
- AWS Dynamodb with pynamodb
- zappa for serverless deployment

## Installation

### Docker

```
git clone https://github.com/ivansabik/ubicajeros-api.git
cd ubicajeros-api
source .venv/bin/activate
pip install -r requirements-deploy.txt
zappa deploy dev
```

### In AWS using zappa

```
git clone https://github.com/ivansabik/ubicajeros-api.git
cd ubicajeros-api
zappa deploy
```

### Manual

```
git clone https://github.com/ivansabik/ubicajeros-api.git
cd ubicajeros-api
virtualenv .venv #optional
source .venv/bin/activate #optional
pip install -r requirements.txt
python ubicajeros/api.py
```

To update the db:

```
python bin/update_db.py -h
usage: update_db.py [-h] [-r RADIUS] [-l LATLON]

Update db with Cajeros

optional arguments:
  -h, --help            show this help message and exit
  -r RADIUS, --radius RADIUS
                        Search radius (this is in km.)
  -l LATLON, --latlon LATLON
                        Latitude/Logitude separated by comma
```

You can run a demo client app at `/cajeros.html`

## Endpoints

- /cajeros
- /cajero/ID_CAJERO

### /cajero/J16621

```javascript
{
  "address": "FRANCISCO_I_MADERO, 20, CENTRO, Cuauht\u00e9moc, Distrito Federal",
  "id": "A00044",
  "lat": 19.433838,
  "lon": -99.138858,
  "open_hours": "06:00-14:00",
  "org_code": 40042,
  "org_name": "MIFEL",
  "updated_at": "Sun, 16 Jul 2017 05:14:36 GMT",
  "zip_code": "6000"
}
```

### /cajeros

```javascript
{
  "cajeros": [
    {
      "address": "BOLIVAR No 38, 38, CENTRO, Venustiano Carranza, Distrito Federal",
      "id": "2775",
      "lat": 19.431813,
      "lon": -99.138561,
      "open_hours": "00:00-24:00",
      "org_code": 40012,
      "org_name": "BBVA BANCOMER",
      "updated_at": "Sun, 16 Jul 2017 05:14:36 GMT",
      "zip_code": "15000"
    },
    {
      "address": "Francisco I. Madero, No 6, Centro, Cuauht\u00e9moc, Distrito Federal",
      "id": "QMXS75",
      "lat": 19.434148,
      "lon": -99.138034,
      "open_hours": "08:00-22:00",
      "org_code": 40036,
      "org_name": "INBURSA",
      "updated_at": "Sun, 16 Jul 2017 05:14:36 GMT",
      "zip_code": "6500"
    }
  ]
}
```

### /cajeros?estado=tabasco

Returns only values for this state
