from flask import Flask, jsonify
from ediplug.ediplug import SmartPlug
import os

app = Flask(__name__)

host = os.getenv('HOST')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

ediplug = SmartPlug(host, (username, password))


@app.route("/")
@app.route("/info")
def info():
    return jsonify(device=ediplug.info, state=ediplug.state)


@app.route("/status")
def status():
    return jsonify(state=ediplug.state)


@app.route("/schedule")
def schedule():
    return jsonify(ediplug.schedule)


@app.route("/toggle", methods = ['GET', 'POST'])
def toggle():
    requested_state = 'ON' if ediplug.state == 'OFF' else 'OFF'
    ediplug.state = requested_state
    return jsonify(state=ediplug.state)


@app.route("/on", methods = ['GET', 'POST'])
def power_on():
    requested_state = 'ON'
    ediplug.state = requested_state
    return jsonify(state=ediplug.state)


@app.route("/off", methods = ['GET', 'POST'])
def power_off():
    requested_state = 'OFF'
    ediplug.state = requested_state
    return jsonify(state=ediplug.state)


@app.route("/usage")
def usage():
    return jsonify(current=ediplug.current, wattage=ediplug.power)


if __name__ == '__main__':
    app.run(port=4999)