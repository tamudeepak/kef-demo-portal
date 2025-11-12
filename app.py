from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    featured = [
        {"title": "Lyric Studio Wireless", "desc": "Compact high-fidelity speaker with warm mids.", "price": 299.00, "img": "https://via.placeholder.com/600x400?text=Lyric+Studio"},
        {"title": "Pulse Rock Subwoofer", "desc": "Deep bass subwoofer for small to medium rooms.", "price": 449.00, "img": "https://via.placeholder.com/600x400?text=Pulse+Subwoofer"},
        {"title": "Studio Monitor 2", "desc": "Reference monitor for accurate studio mixing.", "price": 799.00, "img": "https://via.placeholder.com/600x400?text=Studio+Monitor"},
    ]
    return render_template("index.html", featured=featured)

if __name__ == "__main__":
    # For easy local testing, debug=True. Remove in production.
    app.run(host="0.0.0.0", port=5000, debug=True)
