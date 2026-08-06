import sqlite3

def init_db():
    conn = sqlite3.connect('reviews.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            album_id TEXT,
            name TEXT,
            artist TEXT,
            art TEXT,
            rating REAL,
            review TEXT
            )""")

    conn.commit()
    conn.close()

def save_review(album_id, name, artist, art, rating, review):
    conn = sqlite3.connect('reviews.db')
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO reviews
    (album_id, name, artist, art, rating, review)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        album_id,
        name,
        artist,
        art,
        rating,
        review
    ))

    conn.commit()
    conn.close()

def get_reviews(album_id):
    conn = sqlite3.connect('reviews.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT rating, review 
        FROM reviews 
        WHERE album_id = ?
    """, (album_id,))
    reviews = cursor.fetchall()
    conn.close()
    return reviews

def get_all_reviews():
    conn = sqlite3.connect('reviews.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, artist, art, rating, review
        FROM reviews
    """)
    reviews = cursor.fetchall()
    conn.close()
    return reviews

def has_reviews(album_id):
    conn = sqlite3.connect('reviews.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id 
        FROM reviews 
        WHERE album_id = ?
    """, (album_id,))
    review = cursor.fetchone()
    conn.close()
    return review is not None

if __name__ == "__main__":
    init_db()
