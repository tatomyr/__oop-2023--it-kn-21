from flask import Flask, jsonify, request, send_file, render_template
from flask_cors import CORS
from musicLoader import MusicLoader
from service import DeezerService

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

URL = 'http://localhost:5001/'

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

musicLoader = MusicLoader()
ser = DeezerService()

# sanity check route
@app.route('/getMusicData', methods=['GET'])
def getMusicData():
    position = request.args.get('pos', type=int)
    songs = musicLoader.load_tracks()
    if position == None or position < 0 or position > len(songs):
        position = 0
    song = songs[position]
    metadata = musicLoader.get_metadata(song)
    metadata['cover'] = URL + metadata['cover']
    metadata['file'] = URL + song
    metadata['max'] = len(songs) - 1
    return jsonify(metadata)
    # return jsonify('/src/assets/album_cover.png')

@app.route('/getAll', methods=['GET'])
def getAll():
    songs = musicLoader.load_tracks()
    metadata = []
    for song in songs:
        metadata.append(musicLoader.get_metadata(song))
    return jsonify(metadata)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', type=str)
    songs = ser.search_music(query)
    return jsonify(songs)

@app.route('/download', methods=['POST'])
def download():
    song = request.args.get('songId', type=int)
    status = ser.start_downloading(song, t='id')
    return jsonify(status)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def send_song(path):
    return send_file(path)


if __name__ == '__main__':
    app.run(host='localhost', port='5001')