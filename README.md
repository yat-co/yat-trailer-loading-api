# YAT Trailer Loading API

## Install

## Usage


### Start Server Option 1:  Docker Hosted

Docker
```
docker-compose -f docker-compose.yaml build --no-cache && docker-compose -f docker-compose.yaml up

echo detached
docker-compose -f docker-compose.yaml build --no-cache && docker-compose -f docker-compose.yaml up -d
```
Use `port=80`.

### Start Server Option 2:  Machine Hosted
Navigate to the root directory of the repo, and run:
```
python main.py
```
Use the `API_PORT` environment variable set in `.env` for `port`.  In the sample, it's `port=5000`.

### Calling the API
You can call the API from any application you like.  Here is an example in Python code.  In a Python IDE or shell:

#### Setup
```
import requests

port = 5000
base_url = f'http://127.0.0.1:{port}/'

shipment_list = [
    {
        "length": 40,
        "width": 42,
        "height": 35,
        "weight": 300,
        "packing": "PALLET",
        "stack_limit": 2,
        "num_pieces": 5
    },
    {
        "length": 46,
        "width": 40,
        "height": 30,
        "weight": 250,
        "packing": "BOX",
        "stack_limit": 3,
        "num_pieces": 6
    }
]
```

#### Optimization using equipment type
```
request_data = {
    'equipment_code' : 'DV_53',
    'shipment_list' : shipment_list,
    'allow_rotations' : True
}
url = f'{base_url}api/ytl/optimize-trailer-load/'
response = requests.post(url,json=request_data)
response.status_code,response.json()
```

#### Optimization using trailer dims
```
trailer_dims = {
    "inner_width": 98.5,
    "inner_length": 630,
    "inner_height": 108,
    "max_weight": 42500
}
request_data = {
    'trailer_dims' : trailer_dims,
    'shipment_list' : shipment_list,
    'allow_rotations' : True
}
url = f'{base_url}api/ytl/optimize-trailer-load/'
response = requests.post(url,json=request_data)
response.status_code,response.json()
```

#### Equipment type options
```
url = f'{base_url}api/ytl/equipment-options/'
response = requests.get(url)
response.status_code,response.json()
```

#### Packing type options
```
url = f'{base_url}api/ytl/packing-type-options/'
response = requests.get(url)
response.status_code,response.json()
```
