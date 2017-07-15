from __future__ import absolute_import
import argparse
import traceback

import requests

from ubicajeros import const
from ubicajeros.models import create_tables, Cajero


def _assign_state(address):
    for state in const.STATES:
        if (',' + state).replace(' ', '') in address.upper().replace(' ', ''):
            return state
        elif state.replace(' ', '') in address[-19:].replace(' ', ''):
            return state
    return 'N/A'


def _get_cajeros(latlon, radius):
    url_cajeros = 'http://www.banxico.org.mx/consultas-atm/cajeros.json?l={}&b=&r={}'.format(latlon, radius)
    url_cajero = 'http://www.banxico.org.mx/consultas-atm/cajeros/info.json'

    print('Getting ' + url_cajeros)
    cajeros_json = requests.get(url_cajeros).json()['contenido']
    total_cajeros = len(cajeros_json)

    agregados = 0
    create_tables()
    for i, cajero_json in enumerate(cajeros_json):
        cajero = Cajero()
        cajero.id = cajero_json['id']
        cajero.org_code = cajero_json['cb']
        cajero.lat = cajero_json['l']['lat']
        cajero.lon = cajero_json['l']['lng']
        cajero.org_name = const.ORG_NAMES[cajero.org_code]

        print('Cajero ' + str(i) + ' out of ' + str(total_cajeros))
        url_cajero = '{}?id={}&banco={}'.format(url_cajero, cajero.id, cajero.org_code)
        try:
            response = requests.get(url_cajero)
            cajero_json = response.json()['contenido']
        except:
            traceback.print_exc()
            print(response.content)
            continue
        cajero.zip_code = str(cajero_json['cp'])
        cajero.open_hours = cajero_json['hs']
        cajero.address = cajero_json['d']
        cajero.state = _assign_state(cajero.address)

        cajero.save()

        agregados += 1
        print('Added: {}'.format(cajero.__dict__))

    print('Added: ' + str(agregados))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update db with Cajeros')
    parser.add_argument('-r', '--radius', required=False, help='Search radius (this is in km.)',
                        default='1000')
    parser.add_argument('-l', '--latlon', required=False, help='Latitude/Logitude separated by comma',
                        default='19.432608,-99.133209')  # Tenochtitlan by default

    args = parser.parse_args()

    _get_cajeros(args.latlon, args.radius)
