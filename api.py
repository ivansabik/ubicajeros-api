from flask import Flask, jsonify, request
from flask.ext.cors import CORS
from unqlite import UnQLite

app = Flask(__name__)
CORS(app)

db = UnQLite('cajeros.db', open_database=True)

LIMITE = 1000


# Pasar a script de actualizar db
def _asigna_estado(direccion):
    ESTADOS = ['AGUASCALIENTES', 'BAJA CALIFORNIA SUR', 'BAJA CALIFORNIA', 'CAMPECHE', 'CHIAPAS',
               'CHIHUAHUA', 'DISTRITO FEDERAL', 'COAHUILA', 'COLIMA', 'DURANGO', 'GUANAJUATO',
               'GUERRERO', 'HIDALGO', 'JALISCO', 'ESTADO DE MEXICO', 'MICHOACAN', 'MORELOS',
               'NAYARIT', 'NUEVO LEON', 'OAXACA', 'PUEBLA', 'QUERETARO', 'QUINTANA ROO',
               'SAN LUIS POTOSI', 'SINALOA', 'SONORA', 'TABASCO', 'TAMAULIPAS', 'TLAXCALA',
               'VERACRUZ', 'YUCATAN', 'ZACATECAS']
    for estado in ESTADOS:
        if (',' + estado).replace(' ', '') in direccion.upper().replace(' ', ''):
            return estado
        elif estado.replace(' ', '') in direccion[-19:].replace(' ', ''):
            return estado
    return 'N/A'


@app.route('/api/v1/cajeros')
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
            cajero['estado'] = _asigna_estado(cajero['direccion'])
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


@app.route('/api/v1/cajero/<id>')
def cajero(id):
    if db.exists(id):
        cajero = db[id]
        cajero = eval(cajero)
        cajero['estado'] = _asigna_estado(cajero['direccion'])
        return jsonify(cajero)
    else:
        error = {'mensaje_error': 'No existen cajeros con id' + str(id)}
        return jsonify(error)

if __name__ == '__main__':
    app.run(debug=True)
