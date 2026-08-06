from flask import Flask, render_template, request, url_for, redirect
from spotify_api import get_album, search_albums
from image_colors import get_dom_color
from database import save_review, get_reviews

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# All rankings page route
@app.route('/all_rankings')
def all_rankings():
    return render_template('all_rankings.html')

# Album ranking form page route
@app.route('/album/<album_id>', methods=["GET", "POST"])
def album_review(album_id):
    spotify_data = get_album(album_id)
    reviews = get_reviews(album_id)

    if request.method == "POST":
        rating = float(request.form.get("rating"))
        review = request.form.get("review")
        save_review(album_id, rating, review)

        return redirect(url_for('ranking', album_id=album_id))

    color = get_dom_color(spotify_data['art'])
    color = f"rgb{color}"
    return render_template('ranking_form.html', spotify=spotify_data, color=color, reviews=reviews)

# Personal ranking page route
@app.route('/ranking/<album_id>')
def ranking(album_id):
    spotify_data = get_album(album_id)
    reviews = get_reviews(album_id)

    return render_template('ranking.html', spotify=spotify_data, reviews=reviews)
    

# Search results page route
@app.route('/search_results')
def search_results():
    return render_template('search_results.html')

# Search page route
@app.route('/search')
def search():
    query = request.args.get("query")

    if not query or not query.strip():
        return render_template('search.html')

    results = search_albums(query)

    return render_template('search_results.html', albums=results)

if __name__ == '__main__':
    app.run(debug=True)