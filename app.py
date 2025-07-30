from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from {os.getenv('APP_NAME', 'MyApp')}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
