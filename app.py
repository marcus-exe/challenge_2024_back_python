from flask import Flask
from google_module import gemini_api

app = Flask(__name__)

@app.route('/')
def home():
    return gemini_api.hello_from_gemini()

if __name__ == '__main__':
    app.run(debug=True)
