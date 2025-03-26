# StreamFinder - Universal Streaming Search

StreamFinder is a modern web application that helps users find where to watch their favorite movies and TV shows across various streaming platforms. Built with Flask and vue.js, it provides a sleek, user-friendly interface to search and discover streaming availability.

## Features

- 🎬 Search for both movies and TV shows
- 🔍 Real-time search suggestions
- 📱 Responsive design for all devices
- 🎯 Quick access to streaming service availability
- ⭐ View ratings and release dates
- 🔄 Toggle between movies and TV shows

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: Vue.js 3
- **Styling**: CSS3 with Bootstrap 5
- **APIs**: TMDb API for movie and TV show data
- **Icons**: Font Awesome
- **Fonts**: Inter & Montserrat (Google Fonts)

## Getting Started

### Prerequisites

- Python 3.7+
- Node.js 14+
- TMDb API key ([Get one here](https://www.themoviedb.org/documentation/api))

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bcentner/streamfinder.git
   cd streamfinder
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   npm install # for frontend dependencies
   ```

4. Create a `.env` file in the project root and add your TMDb API key:
   ```
   TMDB_API_KEY=your_api_key_here
   ```

5. Run the application:
   ```bash
   flask run
   # or
   python app.py
   ```

6. Open your browser and navigate to http://127.0.0.1:5000

## Project Structure

## Environment Variables
The application requires the following environment variable:
TMDB_API_KEY: Your TMDb API key (get one at themoviedb.org)

## Development
To run the application in development mode:

## License
This project is licensed under the MIT License - see the LICENSE file for details.