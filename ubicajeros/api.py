import os

from flask import Flask, jsonify, request

from ubicajeros import const
from ubicajeros.models import create_tables_if_not_exist, Cajero

app = Flask(__name__)

results_limit = int(os.environ.get('RESULTS_LIMIT', '1000'))


@app.before_first_request
def setup():
    create_tables_if_not_exist()


@app.route('/cajeros')
def cajeros():
    latlon = request.args.get('latlon')
    state = request.args.get('state')
    cajeros = []
    if state:
        for cajero in Cajero.scan(state__contains=state.upper()):
            cajeros.append(cajero.to_dict())
    elif latlon:
        # To be implemented!
        pass
    else:
        for cajero in Cajero.scan(limit=const.RESULTS_LIMIT):
            cajeros.append(cajero.to_dict())
    return jsonify({'cajeros': cajeros})


@app.route('/cajero/<id>')
def cajero(id):
    try:
        cajero = Cajero.get(id)
        return jsonify(cajero.to_dict())
    except Cajero.DoesNotExist:
        error = {'error_message': 'No Cajero exists with ID {}'.format(id)}
        return jsonify(error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
