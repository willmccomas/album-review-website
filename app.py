from flask import Flask, render_template
from spotify_api import get_album
from image_colors import get_dom_color

app = Flask(__name__)

albums = [
    {
        "title": "Rodeo",
        "artist": "Travis Scott",
        "rating": 10
    },
    {
        "title": "Blonde",
        "artist": "Frank Ocean",
        "rating": 10
    },
    {
        "title": "Die Lit",
        "artist": "Playboi Carti",
        "rating": 9
    },
    {
        "title": "ASTROWORLD",
        "artist": "Travis Scott",
        "rating": 9
    },
    {
        "title": "xperiment",
        "artist": "Ken Carson",
        "rating": 8
    },
    {
        "title": "Maverick \"Almost Forever\"",
        "artist": "Lil Uzi Vert",
        "rating": 7
    },
    {
        "title": "The Life of Pablo",
        "artist": "Kanye West",
        "rating": 6
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/albums')
def albums_page():
    return render_template('albums.html', albums=albums)

@app.route('/album/<album_name>')
def album_review(album_name):
    album = next((a for a in albums if a["title"].lower().replace(' ', '-') == album_name), None)
    if album:
        spotify_data = get_album(album["title"], album["artist"])
        color = get_dom_color(spotify_data["art"])
        color = f"rgb{color}"
        return render_template('review.html', album=album, spotify = spotify_data, color = color)
    return "Album not found"

if __name__ == '__main__':
    app.run(debug=True)