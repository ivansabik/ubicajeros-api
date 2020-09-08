import os

from flask import Flask, jsonify, render_template, request

from ubicajeros.models import create_tables_if_not_exist, Cajero

app = Flask(__name__)

API_URL = os.environ.get("API_URL", "http://localhost:5000")
RESULTS_LIMIT = int(os.environ.get("RESULTS_LIMIT", "1000"))
GMAPS_API_KEY = os.environ.get("GMAPS_API_KEY")


@app.before_first_request
def setup():
    create_tables_if_not_exist()


@app.route("/cajeros.html")
def view_cajeros():
    return render_template("cajeros.html", api_url=API_URL, gmaps_api_key=GMAPS_API_KEY)


@app.route("/cajeros")
def cajeros():
    latlon = request.args.get("latlon")
    state = request.args.get("state")
    cajeros = []
    if state:
        for cajero in Cajero.scan(state__contains=state.upper()):
            cajeros.append(cajero.to_dict())
    elif latlon:
        # To be implemented!
        pass
    else:
        for cajero in Cajero.scan(limit=RESULTS_LIMIT):
            cajeros.append(cajero.to_dict())
    return jsonify({"cajeros": cajeros})


@app.route("/cajero/<id>")
def cajero(id):
    try:
        cajero = Cajero.get(id)
        return jsonify(cajero.to_dict())
    except Cajero.DoesNotExist:
        error = {"error_message": "No Cajero exists with ID {}".format(id)}
        return jsonify(error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
