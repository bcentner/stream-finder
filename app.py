from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
try:
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

app = Flask(__name__, static_url_path="/stream-finder/static")

# Get API key from environment variable
TMDB_API_KEY = os.environ.get('TMDB_API_KEY')

if not TMDB_API_KEY:
    print("WARNING: No TMDb API key set. Please set the TMDB_API_KEY environment variable.")
    # Remove this fallback in production
    TMDB_API_KEY = "YOUR_API_KEY_HERE"  # Replace before deployment

@app.route('/')
def index():
    return render_template('index.html')

# API proxy endpoints
@app.route('/api/search/<media_type>')
def search(media_type):
    query = request.args.get('query', '')
    
    if not query:
        return jsonify({"results": []}), 400
    
    url = f"https://api.themoviedb.org/3/search/{media_type}"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "query": query,
        "page": request.args.get('page', '1'),
        "include_adult": "false"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e), "results": []}), 500

@app.route('/api/providers/<media_type>/<int:id>')
def providers(media_type, id):
    url = f"https://api.themoviedb.org/3/{media_type}/{id}/watch/providers"
    params = {
        "api_key": TMDB_API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e), "results": {}}), 500

# Add more routes here

if __name__ == '__main__':
    app.run(debug=True) 