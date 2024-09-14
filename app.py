from flask import Flask, request
from google_module import gemini_api

app = Flask(__name__)


# Home Page
@app.route('/')
def home():
    return "Index Page"

# Request Page
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json  # Access POST data
    # Here we use gemini stuff
    return f"Received data: {data}"

if __name__ == '__main__':
    app.run(debug=True)
