import os

from flask import Flask, jsonify, request

from models import create_tables

app = Flask(__name__)

LIMIT = int(os.environ.get('RESULTS_LIMIT', '1000'))


@app.before_first_request
def setup():
    create_tables()


@app.route('/cajeros')
def cajeros():
    latlon = request.args.get('latlon')
    cp = request.args.get('cp')
    direccion = request.args.get('direccion')
    estado = request.args.get('estado')
    try:
        limite = int(request.args.get('limite'))
        limite_default = False
    except:
        limite = LIMITE
        limite_default = True
    cajeros = []
    for clave, cajero in [item for item in db]:
        try:
            cajero = eval(cajero)
            if estado:
                if estado.upper() in cajero['estado']:
                    cajeros.append(cajero)
                else:
                    pass
            # Sin filtros
            else:
                cajeros.append(cajero)
        except:
            print cajero
            pass

    if estado and limite_default:
        cajeros = cajeros
    else:
        cajeros = cajeros[0:limite]
    resultados = {'num_resultados': len(cajeros), 'num_cajeros': len(db), 'resultados': cajeros}
    return jsonify(resultados)


@app.route('/cajero/<id>')
def cajero(id):
    if db.exists(id):
        cajero = db[id]
        cajero = eval(cajero)
        return jsonify(cajero)
    else:
        error = {'mensaje_error': 'No existen cajeros con id' + str(id)}
        return jsonify(error)


if __name__ == '__main__':
    app.run(debug=True)
