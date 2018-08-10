from flask import Blueprint

blueprint = Blueprint("index", __name__)

@blueprint.route("/")
def base_url():
    return redirect(url_for("index"))

@blueprint.route("/index")
def index():
    return render_template("index/index.html", apiKey=config.apiKey)
