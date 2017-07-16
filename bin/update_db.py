from __future__ import absolute_import
import argparse

from ubicajeros import const, utils


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update db with Cajeros')
    parser.add_argument('-r', '--radius', required=False, help='Search radius (this is in km.)',
                        default=const.DEFAULT_SEARCH_RADIUS)
    parser.add_argument('-l', '--latlon', required=False, help='Latitude/Logitude separated by comma',
                        default=const.DEFAULT_LAT_LON)  # Tenochtitlan by default

    args = parser.parse_args()

    utils.get_cajeros(args.latlon, args.radius)
