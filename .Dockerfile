FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY requirements.txt ./

RUN python -m pip install pip --upgrade
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app