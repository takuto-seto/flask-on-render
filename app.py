from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello world"

# ローカル開発用
if __name__ == "__main__":
    import os

    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
