from flask import Blueprint, redirect, render_template, url_for

from config import args as config

blueprint = Blueprint("index", __name__)

@blueprint.route("/")
def base_url():
    return redirect(url_for(".index"))

@blueprint.route("/index")
def index():
    return render_template("index/index.html", apiKey=config.apiKey)
