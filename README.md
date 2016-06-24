API ubicajeros
===========

Basado en la app ubicajeros de BANXICO, hay mucha información mal sobre todo de latlon de las ubicaciones entonces repórtenla en la app para que la corrijan y nos sirva mejor a todos.

```
git clone https://github.com/ivansabik/ubicajeros-api.git
cd ubicajeros-api
pip install -r requirements.txt
```

Primero puedes actualizar la base de datos:

```
python actualizar_db.py -h
usage: actualizar_db.py [-h] [-r RADIO] [-l LATLON]

Ubicajeros API actualizar db

optional arguments:
  -h, --help            show this help message and exit
  -r RADIO, --radio RADIO
                        Radio de busqueda en kms.
  -l LATLON, --latlon LATLON
                        Latlon de busqueda
```

Si quieres obtener todos los cajeros nuevamente desde cero borra el archivo `cajeros.db` y corre `python actualizar_db.py`.

Para iniciar la API:

```
python api.py
```

Puedes hacer llamadas en `http://localhost:5000/api/v1`.

## App demo (cliente_demo.html)



## Endpoints

- /api/v1/cajeros
- /api/v1/cajero/ID_CAJERO

### /api/v1/cajero/J16621

```javascript
{
  "actualizacion": "2016-05-08 17:30:02.114600",
  "clave_institucion": 37166,
  "cp": "86500",
  "direccion": "Pasaje Cinema C\u00e1rdenas Loc. 2,SN,Centro,C\u00e1rdenas,Tabasco",
  "estado": "TABASCO",
  "horario": "08:30-16:30",
  "id": "J16621",
  "lat": 17.98894,
  "lon": -93.37776,
  "nombre_institucion": "BANSEFI"
}
```

### /api/v1/cajeros?limite=2

```javascript
{
  "num_cajeros": 434,
  "num_resultados": 2,
  "resultados": [
    {
      "actualizacion": "2016-05-08 17:30:18.002034",
      "clave_institucion": 40002,
      "cp": "56600",
      "direccion": "AV. TEZOZOMOC,S/N,ALFREDO BARRANDA,CHALCO,ESTADO DE MEXICO",
      "estado": "ESTADO DE MEXICO",
      "horario": "00:00-23:59",
      "id": "4190-VALLEDEC",
      "lat": 19.2779192,
      "lon": -98.946103,
      "nombre_institucion": "BANAMEX"
    },
    {
      "actualizacion": "2016-05-08 17:30:16.196350",
      "clave_institucion": 40002,
      "cp": "31380",
      "direccion": "BLVD. VICENTE LOMBARDO TOLEDANO,4800,CONCORDIA,CHIHUAHUA,CHIHUAHUA",
      "estado": "CHIHUAHUA",
      "horario": "00:00-23:59",
      "id": "4176-ALSUPERRO",
      "lat": 28.6511284,
      "lon": -106.02612,
      "nombre_institucion": "BANAMEX"
    }
  ]
}
```

### /api/v1/cajeros?estado=distrito&limite=2

```javascript
{
  "num_cajeros": 434,
  "num_resultados": 2,
  "resultados": [
    {
      "actualizacion": "2016-05-08 17:30:18.743436",
      "clave_institucion": 40002,
      "cp": "2830",
      "direccion": "AV. CUITLAHUAC,3423,SAN BERNABE,AZCAPOTZALCO,DISTRITO FEDERAL",
      "estado": "DISTRITO FEDERAL",
      "horario": "00:00-23:59",
      "id": "5524-CUITLAHUAC",
      "lat": 19.470294,
      "lon": -99.170741,
      "nombre_institucion": "BANAMEX"
    },
    {
      "actualizacion": "2016-05-08 17:30:15.066023",
      "clave_institucion": 40002,
      "cp": "6020",
      "direccion": "MANUEL DOBLADO,10,CENTRO,CUAUHTEMOC,DISTRITO FEDERAL",
      "estado": "DISTRITO FEDERAL",
      "horario": "00:00-23:59",
      "id": "1942-PLAZAMIXC",
      "lat": 19.6264846,
      "lon": -99.297088,
      "nombre_institucion": "BANAMEX"
    }
  ]
}
```
