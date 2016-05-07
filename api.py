import locale
from flask import Flask, jsonify, request
from unqlite import UnQLite

app = Flask(__name__)
db = UnQLite('cajeros.db', open_database=True)

LIMITE = 1000

@app.route('/api/v1/cajeros')
def cajeros():
    empresa = request.args.get('empresa')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    nombre = request.args.get('nombre')
    direccion = request.args.get('direccion')
    try:
        limite = int(request.args.get('limite'))
    except:
        limite = LIMITE
    cajeros = []
    for clave, cajero in [item for item in db]:
        if len(cajeros) >= limite:
            break
        cajero = eval(cajero)
        cajeros.append(cajero)
    resultados = {'resutados': cajeros, 'numero_cajeros': len(db)}
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
