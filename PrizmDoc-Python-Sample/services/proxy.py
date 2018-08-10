from flask import Blueprint

blueprint = Blueprint("proxy", __name__)

@blueprint.route("/pas")
def proxy():
    
