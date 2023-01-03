from flask import Flask, request, make_response
from flask_cors import CORS

from decouple import config
import logging
from typing import Dict

from ytl import optimize_trailer_load_plan_wrapper
from ytl.optimizer_functions import PIECE_ARRANGEMENT_ROUTER, SHIPMENT_ARRANGEMENT_ROUTER
from ytl.standard_logistic_dims import STANDARD_TRAILER_DIMS
from ytl.options import PACKING_OPTIONS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Logging
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
logger = logging.getLogger(__name__)

fileHandler = logging.FileHandler("./logs/ytl.log")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

def json_response(data='', status: int = 200, headers: Dict = None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = 'application/json'
    return make_response(data, status, headers)

@app.route('/api/ytl/optimize-trailer-load/', methods=['POST'])
def trailer_load_optimize():
    if request.method == 'POST':
        status_code,response = optimize_trailer_load_plan_wrapper(request.json)
        return json_response(data=response, status=status_code)
    return json_response(data={'error' : f'Request type {request.method} not accepted'}, status=400)

@app.route('/api/ytl/equipment-options/', methods=['GET'])
def trailer_load_equipment_options():
    if request.method == 'GET':
        return json_response(data=STANDARD_TRAILER_DIMS, status=200)
    return json_response(data={'error' : f'Request type {request.method} not accepted'}, status=400)


@app.route('/api/ytl/packing-type-options/', methods=['GET'])
def trailer_load_packing_options():
    if request.method == 'GET':
        res = [
            {
                'code' : a,
                'name' : b,
            } for a,b in PACKING_OPTIONS
        ]
        return json_response(data=res, status=200)
    return json_response(data={'error' : f'Request type {request.method} not accepted'}, status=400)

@app.route('/api/ytl/piece-arrangement-algorithm-options/', methods=['GET'])
def trailer_load_piece_arrangement_algorithm_options():
    if request.method == 'GET':
        res = [b for a,b in PIECE_ARRANGEMENT_ROUTER.values()]
        return json_response(data=res, status=200)
    return json_response(data={'error' : f'Request type {request.method} not accepted'}, status=400)

@app.route('/api/ytl/shipment-arrangement-algorithm-options/', methods=['GET'])
def trailer_load_shipment_arrangement_algorithm_options():
    if request.method == 'GET':
        res = [b for a,b in SHIPMENT_ARRANGEMENT_ROUTER.values()]
        return json_response(data=res, status=200)
    return json_response(data={'error' : f'Request type {request.method} not accepted'}, status=400)

if __name__ == "__main__":
    app.run(
        host=config("API_HOST", cast=str, default="0.0.0.0"),
        port=config("API_PORT", cast=int, default=80),
        debug=config("DEBUG", cast=bool, default=True)
    )
