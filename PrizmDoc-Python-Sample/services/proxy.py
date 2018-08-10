from flask import Blueprint, request

blueprint = Blueprint("proxy", __name__)

@blueprint.route("/pas")
def proxy():

