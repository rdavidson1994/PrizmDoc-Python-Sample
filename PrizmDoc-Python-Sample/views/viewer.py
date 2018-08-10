from flask import Blueprint, render_template

blueprint = Blueprint("viewer", __name__)

@blueprint.route("/viewer")
def viewer():
    return render_template("viewer/viewer.html")
