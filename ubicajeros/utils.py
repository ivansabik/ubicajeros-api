from __future__ import absolute_import
import traceback

import requests

from ubicajeros import const
from ubicajeros.models import create_tables_if_not_exist, Cajero


def _assign_state(address):
    for state in const.STATES:
        if ("," + state).replace(" ", "") in address.upper().replace(" ", ""):
            return state
        elif state.replace(" ", "") in address[-19:].replace(" ", ""):
            return state
    return "N/A"


def _get_cajero(cajero_json):
    cajero = Cajero()
    cajero.id = cajero_json["id"]
    cajero.org_code = cajero_json["cb"]
    cajero.lat = cajero_json["l"]["lat"]
    cajero.lon = cajero_json["l"]["lng"]
    cajero.org_name = const.ORG_NAMES[cajero.org_code]

    url_cajero = "{}?id={}&banco={}".format(
        const.BASE_URL_CAJERO, cajero.id, cajero.org_code
    )
    print("Getting {}".format(url_cajero))
    try:
        response = requests.get(url_cajero)
        cajero_json = response.json()["contenido"]
    except:
        traceback.print_exc()
        print(response.content)
        return
    cajero.zip_code = str(cajero_json["cp"])
    cajero.open_hours = cajero_json["hs"]
    cajero.address = cajero_json["d"]
    cajero.state = _assign_state(cajero.address)

    cajero.save()

    print("Added: {}".format(cajero.__dict__))
    return Cajero


def get_cajeros(latlon=const.DEFAULT_LAT_LON, radius=const.DEFAULT_SEARCH_RADIUS):
    url_cajeros = "http://www.banxico.org.mx/consultas-atm/cajeros.json?l={}&b=&r={}&c=true".format(
        latlon, radius
    )
    print("Getting " + url_cajeros)
    cajeros_json = requests.get(url_cajeros)
    try:
        cajeros_json = cajeros_json.json()
    except ValueError:
        raise Exception("Unable to parse response: {}".format(cajeros_json.content))
    else:
        cajeros_json = cajeros_json["contenido"]
    total_cajeros = len(cajeros_json)

    create_tables_if_not_exist()
    for i, cajero_json in enumerate(cajeros_json):
        print("Cajero {} out of {}".format(i + 1, total_cajeros))
        try:
            Cajero.get(cajero_json["id"])
            print("Cajero {} already exists in db".format(cajero_json["id"]))
            continue
        except Cajero.DoesNotExist:
            try:
                _get_cajero(cajero_json)
            except:
                print(cajero_json)
                traceback.print_exc()
                continue
        except:
            print(cajero_json)
            traceback.print_exc()
            continue
