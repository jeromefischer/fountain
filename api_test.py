import flask
from flask import jsonify, request

from FlowMeter import FlowMeter
from TemperatureSensor import TemperatureSensor

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
sensors = [
    {'sensor_location': 'water',
     'temeraure': 18.2},
    {'sensor_location': 'cubicle',
     'temeraure': 19.2}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1>" \
           "<p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/resource/valve/post_on', methods=['POST'])
def api_set_valve_on():
    pass

@app.route('/api/v1/resource/valve/post_off', methods=['POST'])
def api_set_valve_off():
    pass

def api_get_valve_status():
    pass

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/temperature/all', methods=['GET'])
def api_all():
    TS = TemperatureSensor(location='water', sensor_type='DS18B20', sensor_name='/sys/bus/w1/devices/28-01131a6b6e1c/w1_slave')
    return jsonify(TS.read_temp())


@app.route('/api/v1/resources/temperature', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'sensor_location' in request.args:
        location = request.args['sensor_location']
    else:
        return "Error: No location field provided. Please specify a location."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for s in sensors:
        if s['sensor_location'] == location:
            results.append(s)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


app.run(host='192.168.2.11')
