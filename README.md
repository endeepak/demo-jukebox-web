# demo-jukebox-web

Demo jukebox web. Uses https://github.com/endeepak/demo-jukebox-api

Song credits: https://freepd.com

### Run

### Prerequisite

Run API server on using

```sh
docker run -p 5000:5000 -p 8000:8000 endeepak/demo-jukebox-api
```

#### Using code (local)

```sh
# Ensure python 2.x and pip installed
pip install -r app/requirements.txt
python app/server.py
```

#### Using docker

```sh
docker run -p 5001:5001 -p 8001:8001 -e JUKEBOX_API_SERVER_URL=http://<host-ip>:5000 endeepak/demo-jukebox-web
```

### Web

Visit http://localhost:5001/songs/random

### Metrics

Metrics will available in http://localhost:8001
