from flask import Flask, render_template, request
from spotify_api import get_album, search_albums
from image_colors import get_dom_color

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# Album information page route
@app.route('/album/<album_id>')
def album_review(album_id):
    spotify_data = get_album(album_id)
    color = get_dom_color(spotify_data['art'])
    color = f"rgb{color}"
    return render_template('review.html', spotify=spotify_data, color=color)

# Rank page route
@app.route('/rank')
def rank():
    return render_template('rank.html')

# Search page route
@app.route('/search')
def search():
    query = request.args.get("query")

    results = search_albums(query)

    return render_template('search_results.html', albums=results)

if __name__ == '__main__':
    app.run(debug=True)