from argparse import ArgumentParser
from flask import Flask, redirect, render_template, request, url_for

parser = ArgumentParser()

parser.add_argument("--port", default="5000",)
parser.add_argument("--pasUrl", default="localhost",)
parser.add_argument("--pasPort", default="3000",)
parser.add_argument("--apiKey", default="",)

args = parser.parse_args()

app = Flask(__name__, instance_relative_config=True)

@app.route("/")
def base_url():
    return redirect(url_for("index"))

@app.route("/index")
def index():
    return render_template("index/index.html", apiKey=args.apiKey)

@app.route("/viewer")
def viewer():
    return render_template("viewer/viewer.html")

if __name__ == "__main__":
    app.run(port=args.port)
