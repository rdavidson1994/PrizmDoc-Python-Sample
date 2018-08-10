import requests
from flask import Blueprint, request
from config import args as config

blueprint = Blueprint("proxy", __name__)


@blueprint.route("/pas/<arg>")
def proxy(arg):
    # Reverse proxy to sidestep CORS issues.
    header_dict = dict(request.headers)
    header_dict["Accusoft-Secret"] = "mysecretkey"
    url = f"http://localhost:{config.port}/{arg}"
    out_request = requests.request(method=request.method,
                                   url=url,
                                   headers=header_dict,
                                   json=request.get_json())
    return out_request.text
