from flask import Blueprint, request

blueprint = Blueprint("viewingSession", __name__)

@blueprint.route("/viewingSession")
def viewingSession():
