### Orgs

| Org nam       | Code  |
| ------------- | ----- |
| ABC CAPITAL   | 40138 |
| AFIRME        | 40062 |
| AUTOFIN       | 40128 |
| AZTECA        | 40127 |
| BAJIO         | 40030 |
| BANAMEX       | 40002 |
| BANCO FAMSA   | 40131 |
| BANCOPPEL     | 40137 |
| BANJERCITO    | 37019 |
| BANORTE-IXE   | 40072 |
| BANREGIO      | 40058 |
| BANSEFI       | 37166 |
| BANSI         | 40060 |
| BBVA BANCOMER | 40012 |
| BMULTIVA      | 40132 |
| CIBANCO       | 40143 |
| HSBC          | 40021 |
| INBURSA       | 40036 |
| INTERACCIONES | 40037 |
| MIFEL         | 40042 |
| SANTANDER     | 40014 |
| SCOTIABANK    | 40044 |

### Stores

| Comercio       | Clave |
| -------------- | ----- |
| WAL-MART       | 1     |
| MERCO          | 2     |
| CHEDRAUI       | 3     |
| BODEGA AURRERA | 4     |
| SAMS           | 5     |
| SUBURBIA       | 6     |
| SUPERAMA       | 7     |

### cajeros.json

```
curl -o cajeros.json 'https://www.banxico.org.mx/consultas-atm/cajeros.json?l=19.432608,-99.133209&b=&r=1000000000000000000000000000000000000000000000000000000000000'
```

Give something like:

```javascript
{
  "tipoRespuesta": 0,
  "contenido": [
    {
      "id": "T13008",
      "cb": 37019,
      "ta": "01",
      "c": "{\"cr\":\"18.56\"}",
      "r": 0,
      "extra": "{\"bd\":\"1\",\"cnv\":\"\"}",
      "l": {
        "lng": -96.13842,
        "lat": 19.20186
      },
      "t": 0
    }
  ]
}
```

### info.json

```
curl -o info.json 'https://www.banxico.org.mx/consultas-atm/cajeros/info.json?id=6552-SECTELEVI&banco=40002'
```

Gives something linke:

```javascript
{
  "tipoRespuesta": 0,
  "contenido": {
    "extra": "{\"cnv\":[{\"b\":\"37019\",\"cr\":\"0.00\",\"d\":\"Aplica al personal del ejército, fuerza aérea y armada de México, cónyugues y dependientes económicos\"}]}",
    "t": 0,
    "id": "6552-SECTELEVI",
    "cb": 40002,
    "r": 0,
    "cp": "1210",
    "hs": "00:00-23:59",
    "d": "AV. VASCO DE QUIROGA,2000,ZEDEC SANTA FE,ALVARO OBREGON,DISTRITO FEDERAL",
    "re": ""
  },
  "mensajeError": null
}
```
