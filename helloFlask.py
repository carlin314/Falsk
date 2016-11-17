from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!"

@app.route("/flask")
def flask():
    return "Hello flask!!"


if __name__ == "__main__":
    app.run()