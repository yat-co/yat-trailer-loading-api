from pydantic import BaseModel
from typing import List


class Shipment(BaseModel):
    length: float
    width: float
    height: float
    weight: float
    packing: str
    stack_limit: int
    num_pieces: int


class EquipmentShipment(BaseModel):
    equipment_code: str
    allow_rotations: bool
    shipment_list: List[Shipment]
