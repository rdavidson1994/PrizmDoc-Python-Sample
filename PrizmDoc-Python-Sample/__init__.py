from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, instance_relative_config=True)

@app.route("/")
def base_url():
    return redirect(url_for("index"))

@app.route("/index")
def index():
    return render_template("index/index.html", apiKey="")

@app.route("/viewer")
def viewer():
    return render_template("viewer/viewer.html")

if __name__ == "__main__":
    app.run()
