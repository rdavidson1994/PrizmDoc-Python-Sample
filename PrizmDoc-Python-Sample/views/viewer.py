from flask import Blueprint

blueprint = Blueprint("viewer", __name__)

@blueprint.route("/viewer")
def viewer():
    return render_template("viewer/viewer.html")
