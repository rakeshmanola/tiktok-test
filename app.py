from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "TikTok test app running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
