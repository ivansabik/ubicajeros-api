API ubicajeros
===========

Basado en la app ubicajeros de BANXICO, hay mucha información mal sobre todo de latlon de las ubicaciones entonces repórtenla en la app para que la corrijan y nos sirva mejor a todos.

```python actualizar_db.py```

Si quieres actualizar desde cero borra el archivo `cajeros.db`.

Para iniciar la API:

```bash
git clone https://github.com/ivansabik/ubicajeros-api.git
cd ubicajeros-api
pip install -r requirements.txt
python api.py
```


### /api/v1/cajero/000000000005959

```javascript
{
  "clave": 40012,
  "cp": "14200",
  "direccion": "CARRETERA PICACHO AJUSCO 175 , COL. HEROES DE PADIERNA, CIUDAD DE MEXICO, DISTRITO FEDERAL CP. 14200",
  "horario": "00:00-23:59",
  "id": "000000000005959",
  "lat": -99.212138,
  "laton": "-99.212138,19.298659",
  "lon": 19.298659,
  "nombre": "BBVA BANCOMER"
}
```

### /api/v1/cajeros?limite=2

```javascript
{
  "numero_cajeros": 35744,
  "resutados": [
    {
      "clave": 40012,
      "cp": "06000",
      "direccion": "MADERO 70 , COL. CENTRO, CIUDAD DE MEXICO, DISTRITO FEDERAL CP. 06000",
      "horario": "00:00-23:59",
      "id": "000000000000146",
      "lat": -99.134908,
      "laton": "-99.134908,19.433321",
      "lon": 19.433321,
      "nombre": "BBVA BANCOMER"
    },
    {
      "clave": 40002,
      "cp": "93260",
      "direccion": "BLVD. LAZARO CARDENAS,807,MORELOS,POZA RICA,VERACRUZ",
      "horario": "00:00-23:59",
      "id": "3038-PLAZATAJI",
      "lat": -97.464435,
      "laton": "-97.464435,20.524872",
      "lon": 20.524872,
      "nombre": "BANAMEX"
    }
  ]
}
```

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/ivansabik/ubicajeros-api/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
