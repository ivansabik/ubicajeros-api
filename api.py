from flask import Flask, jsonify, request
from flask.ext.cors import CORS
from unqlite import UnQLite

app = Flask(__name__)
CORS(app)

db = UnQLite('cajeros.db', open_database=True)

LIMITE = 1000

@app.route('/api/v1/cajeros')
def cajeros():
    empresa = request.args.get('empresa')
    latlon = request.args.get('lat')
    nombre = request.args.get('nombre')
    cp = request.args.get('cp')  # Buscar CPs cercanos tambien
    direccion = request.args.get('direccion')
    try:
        limite = int(request.args.get('limite'))
    except:
        limite = LIMITE
    cajeros = []
    for clave, cajero in [item for item in db]:
        if len(cajeros) >= limite:
            break
        print cajero
        try:
            cajero = eval(cajero)
            cajeros.append(cajero)
        except:
            print '------'
            print cajero
            print '------'
            pass
    resultados = {'num_resultados': len(cajeros), 'num_cajeros': len(db), 'resultados': cajeros}
    return jsonify(resultados)


@app.route('/api/v1/cajero/<clave>')
def cajero(clave):
    if db.exists(clave):
        cajero = db[clave]
        return jsonify(eval(cajero))
    else:
        error = {'mensaje_error': 'No existen cajeros con clave ' + str(clave)}
        return jsonify(error)

if __name__ == '__main__':
    app.run(debug=True)
