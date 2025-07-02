from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import requests
from dotenv import load_dotenv

try:
    load_dotenv()
except ImportError:
    pass 

app = Flask(__name__, static_url_path="/stream-finder/static")


TMDB_API_KEY = os.environ.get('TMDB_API_KEY')

if not TMDB_API_KEY:
    print("WARNING: No TMDb API key set. Please set the TMDB_API_KEY environment variable.")


print(f"TMDB_API_KEY loaded: {bool(TMDB_API_KEY)}")


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/')
def index():
    return render_template('index.html')


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

# WSGI application wrapper for subdirectory deployment
class PrefixMiddleware:
    def __init__(self, app, prefix='/stream-finder'):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        path_info = environ.get('PATH_INFO', '')
        print(f"PrefixMiddleware: PATH_INFO before: {path_info}, SCRIPT_NAME before: {environ.get('SCRIPT_NAME', '')}")

        if self.prefix and path_info.startswith(self.prefix):
            environ['PATH_INFO'] = path_info[len(self.prefix):] or '/'
            environ['SCRIPT_NAME'] = self.prefix
            
        return self.app(environ, start_response)

# Wrap the app for subdirectory deployment
application = PrefixMiddleware(app)

if __name__ == '__main__':
    app.run(debug=True) 