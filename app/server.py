from flask import Flask, render_template
from flask_prometheus import monitor
import requests
import os
import socket

app = Flask(__name__)

@app.route('/songs/random')
def songs_random():
    jukebox_api_server_url = os.environ.get('JUKEBOX_API_SERVER_URL', 'http://localhost:5000')
    song = requests.get('{}/api/songs/random'.format(jukebox_api_server_url)).json()
    return render_template('song.html', song=song, hostname=socket.gethostname())

monitor(app, port=8001)
app.run(host='0.0.0.0', port=5001)
