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
               'GUERRERO', 'HIDALGO', 'JALISCO', 'ESTADO DE MEXICO', 'MICHOACAN', 'MORELOS', 'NAYARIT',
               'NUEVO LEON', 'OAXACA', 'PUEBLA', 'QUERETARO', 'QUINTANA ROO',
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
    empresa = request.args.get('empresa')
    latlon = request.args.get('lat')
    nombre = request.args.get('nombre')
    cp = request.args.get('cp')  # Buscar CPs cercanos tambien
    direccion = request.args.get('direccion')
    estado = request.args.get('estado')
    try:
        limite = int(request.args.get('limite'))
    except:
        limite = LIMITE
    cajeros = []
    for clave, cajero in [item for item in db]:
        if len(cajeros) >= limite:
            break
        try:
            cajero = eval(cajero)
            cajero['estado'] = _asigna_estado(cajero['direccion'])
            if estado:
                if estado in cajero['estado']:
                    cajeros.append(cajero)
                else:
                    break
            cajeros.append(cajero)
        except:
            print'------'
            print cajero
            print'------'
            pass
    resultados = {'num_resultados': len(cajeros),'num_cajeros': len(db),'resultados': cajeros}
    return jsonify(resultados)


@app.route('/api/v1/cajero/<clave>')
def cajero(clave):
    if db.exists(clave):
        cajero = db[clave]
        cajero = eval(cajero)
        cajero['estado'] = _asigna_estado(cajero['direccion'])
        return jsonify(cajero)
    else:
        error = {'mensaje_error':'No existen cajeros con clave'+ str(clave)}
        return jsonify(error)

if __name__ =='__main__':
    app.run(debug=True)
