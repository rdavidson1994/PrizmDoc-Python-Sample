from flask import Blueprint

blueprint = Blueprint("viewingSession", __name__)

@blueprint.route("/viewingSession")
def viewingSession():
