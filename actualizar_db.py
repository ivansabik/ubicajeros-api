import locale
from unqlite import UnQLite
import pprint
import requests

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

NOMBRES = {
    40138: 'ABC CAPITAL',
    40062: 'AFIRME',
    40128: 'AUTOFIN',
    40127: 'AZTECA',
    40030: 'BAJIO',
    40002: 'BANAMEX',
    40131: 'BANCO FAMSA',
    40137: 'BANCOPPEL',
    37019: 'BANJERCITO',
    40072: 'BANORTE-IXE',
    40058: 'BANREGIO',
    37166: 'BANSEFI',
    40060: 'BANSI',
    40012: 'BBVA BANCOMER',
    40132: 'BMULTIVA',
    40143: 'CIBANCO',
    40021: 'HSBC',
    40036: 'INBURSA',
    40037: 'INTERACCIONES',
    40042: 'MIFEL',
    40014: 'SANTANDER',
    40044: 'SCOTIABANK',
    40134: '',
    40136: '',
    40147: '',
    1: 'WAL-MART',
    2: 'MERCO',
    3: 'CHEDRAUI',
    4: 'BODEGA AURRERA',
    5: 'SAMS',
    6: 'SUBURBIA',
    7: 'SUPERAMA'
}

db = UnQLite('cajeros.db', open_database=True)

RADIO = '99999999999999999999'
CAJEROS_URL = 'http://www.banxico.org.mx/consultas-atm/cajeros.json?l=19.432608,-99.133209&b=&r=' + RADIO
CAJERO_URL = 'http://www.banxico.org.mx/consultas-atm/cajeros/info.json'

print 'Buscando cajeros en ' + CAJEROS_URL
cajeros_json = requests.get(CAJEROS_URL).json()['contenido']
total_cajeros = len(cajeros_json)

for i, cajero_json in enumerate(cajeros_json):
    cajero = {}
    cajero['id'] = cajero_json['id']
    cajero['clave'] = cajero_json['cb']
    cajero['lat'] = cajero_json['l']['lng']
    cajero['lon'] = cajero_json['l']['lat']
    cajero['laton'] = str(cajero['lat']) + ',' + str(cajero['lon'])
    cajero['nombre'] = NOMBRES[cajero['clave']]
    try:
        print 'Cajero ' + str(i) + ' de ' + str(total_cajeros) + ', ' + str(cajero['id']) + ' existe? ' + str(db.exists(cajero['id']))
        if not db.exists(cajero['id']):
            url_cajero = CAJERO_URL + '?id=' + str(cajero['id']) + '&banco=' + str(cajero['clave'])
            cajero_json = requests.get(url_cajero).json()['contenido']
            cajero['cp'] = str(cajero_json['cp'])
            cajero['horario'] = cajero_json['hs']
            cajero['direccion'] = cajero_json['d']
            db[cajero['id']] = cajero
            pprint.pprint(cajero)
    except UnicodeEncodeError:
        print 'UnicodeEncodeError'
        print cajero
        pass
