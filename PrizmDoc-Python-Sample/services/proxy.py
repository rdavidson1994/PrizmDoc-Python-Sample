from flask import Blueprint, request
import requests

from config import args as config

blueprint = Blueprint("proxy", __name__)

@blueprint.route("/pas/<path:arg>", methods=("GET", "POST", "PUT", "DELETE"))
def proxy(arg):
    if config.apiKey == "":
        header_dict = dict(request.headers)

        header_dict["Accusoft-Secret"] = "mysecretkey"

        url = f"http://{config.pasUrl}:{config.pasPort}/{arg}?{request.query_string.decode('utf-8')}"

        out_request = requests.request(method=request.method,
                                       url=url,
                                       headers=header_dict,
                                       data=request.get_data())

        return out_request.text
    else:
        header_dict = dict(request.headers)

        header_dict["Accusoft-Secret"] = "mysecretkey"
        header_dict["acs-api-key"] = config.apiKey

        url = f"https://api.accusoft.com/PCCIS/V1/{arg}?{request.query_string.decode('utf-8')}"

        out_request = requests.request(method=request.method,
                                       url=url,
                                       headers=header_dict,
                                       data=request.get_data())

        return out_request.text
