import argparse
import datetime

from unqlite import UnQLite
import requests

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

parser = argparse.ArgumentParser(description='Ubicajeros API actualizar db')
parser.add_argument('-r', '--radio', required=False, help='Radio de busqueda en kms.', default='1000')
parser.add_argument('-l', '--latlon', required=False, help='Latlon de busqueda', default='19.432608,-99.133209')

args = parser.parse_args()

CAJEROS_URL = 'http://www.banxico.org.mx/consultas-atm/cajeros.json?l=' + args.latlon + '&b=&r=' + args.radio
CAJERO_URL = 'http://www.banxico.org.mx/consultas-atm/cajeros/info.json'

print 'Buscando cajeros en ' + CAJEROS_URL
cajeros_json = requests.get(CAJEROS_URL).json()['contenido']
total_cajeros = len(cajeros_json)

agregados = 0
for i, cajero_json in enumerate(cajeros_json):
    db = UnQLite('cajeros.db')
    db.open()
    cajero = {}
    cajero['id'] = cajero_json['id']
    cajero['clave_institucion'] = cajero_json['cb']
    cajero['lat'] = cajero_json['l']['lat']
    cajero['lon'] = cajero_json['l']['lng']
    cajero['nombre_institucion'] = NOMBRES[cajero['clave_institucion']]
    try:
        print 'Cajero ' + str(i) + ' de ' + str(total_cajeros) + ', ' + str(cajero['id']) + ' existe? ' + str(db.exists(cajero['id']))
        if not db.exists(cajero['id']):
            url_cajero = CAJERO_URL + '?id=' + str(cajero['id']) + '&banco=' + str(cajero['clave_institucion'])
            cajero_json = requests.get(url_cajero).json()['contenido']
            cajero['cp'] = str(cajero_json['cp'])
            cajero['horario'] = cajero_json['hs']
            cajero['direccion'] = cajero_json['d']
            cajero['actualizacion'] = str(datetime.datetime.now())
            db[cajero['id']] = cajero
            print 'Agregado: ' + str(cajero)
            agregados += 1
    except UnicodeEncodeError:
        print 'UnicodeEncodeError'
        print cajero
        pass
    finally:
        db.close()
print 'Cajeros agregados: ' + str(agregados)
