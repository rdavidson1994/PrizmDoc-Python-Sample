from flask import Blueprint, request, redirect
import json
import requests

from config import args as config

blueprint = Blueprint("viewing_session", __name__)

@blueprint.route("/viewingSession")
def viewing_session():
    if request.method == "GET":
        request_type = request.args.get(["type"])
        out_json = {"source": {"type": request_type}}
        if request_type == "document":
            out_json["source"]["fileName"] = request.args.get("document")
        elif request_type == "url":
            out_json["source"]["url"] = request.args.get("url")
        elif request_type == "viewingPackage":
            out_json["source"]["documentId"] = request.args.get("viewingPackage")
        elif request_type is None:
            raise Exception("Missing ?type= parameter")
        else:
            raise Exception("Invalid ?type= parameter")
        url = f"http://localhost:{config.port}/pas/ViewingSession"
        response = requests.post(url=url, json=out_json)
        viewing_session_id = json.loads(response.text)["viewingSessionId"]
        return redirect(f"/viewer?viewingSessionId={viewing_session_id}")

    elif request.method == "POST":
        # TBD, gotta figure out that busboy stuff
        raise NotImplementedError
