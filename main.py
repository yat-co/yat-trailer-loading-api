from fastapi import FastAPI, Response

from ytl.options import PACKING_OPTIONS
from ytl.standard_logistic_dims import STANDARD_TRAILER_DIMS
from ytl.optimizer_functions import PIECE_ARRANGEMENT_ROUTER, SHIPMENT_ARRANGEMENT_ROUTER
from ytl import optimize_trailer_load_plan_wrapper

import logging

from models import EquipmentShipment
from settings import LOGGING_CONFIG

app = FastAPI()

logging.config.dictConfig(LOGGING_CONFIG)


@app.post("/api/ytl/optimize-trailer-load/")
async def trailer_load_optimize(request_data: EquipmentShipment, response: Response):
    status_code, response_data = optimize_trailer_load_plan_wrapper(
        request_data=request_data.model_dump()
    )
    response.status_code = status_code
    return response_data


@app.get("/api/ytl/equipment-options/")
def trailer_load_equipment_options():
    return STANDARD_TRAILER_DIMS


@app.get("/api/ytl/packing-type-options/")
def trailer_load_packing_options():
    return [
        {"code": a, "name": b} for a, b in PACKING_OPTIONS
    ]


@app.get("/api/ytl/piece-arrangement-algorithm-options/")
def trailer_load_piece_arrangement_algorithm_options():
    return [b for a, b in PIECE_ARRANGEMENT_ROUTER.values()]


@app.get("/api/ytl/shipment-arrangement-algorithm-options/")
def trailer_load_shipment_arrangement_algorithm_options():
    return [b for a, b in SHIPMENT_ARRANGEMENT_ROUTER.values()]
