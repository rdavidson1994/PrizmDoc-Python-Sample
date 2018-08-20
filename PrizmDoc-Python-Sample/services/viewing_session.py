from flask import Blueprint, request, redirect
import json
import requests

from config import args as config

blueprint = Blueprint("viewing_session", __name__)

@blueprint.route("/viewingSession", methods=("GET", "POST"))
def viewing_session():
    if request.method == "GET":
        request_type = request.args.get("type")

        post_json = {"source": {"type": request_type}}

        if request_type == "document":
            post_json["source"]["fileName"] = request.args.get("document")
        elif request_type == "url":
            post_json["source"]["url"] = request.args.get("url")
        elif request_type == "viewingPackage":
            post_json["source"]["documentId"] = request.args.get("viewingPackage")

        post_url = f"http://localhost:{config.port}/pas/ViewingSession"

        response = requests.post(url=post_url, json=post_json)

        viewing_session_id = json.loads(response.text)["viewingSessionId"]

        return redirect(f"/viewer?viewingSessionId={viewing_session_id}")
    elif request.method == "POST":
        post_json = {"source": {"type": "upload", "displayName": "upload"}}
        post_url = f"http://localhost:{config.port}/pas/ViewingSession"

        post_response = requests.post(url=post_url, json=post_json)

        viewing_session_id = json.loads(post_response.text)["viewingSessionId"]

        put_url = f"http://localhost:{config.port}/pas/ViewingSession/{viewing_session_id}/SourceFile"

        print(request.files.getlist("uploadInput")[0].read())

        requests.put(url=put_url, data={"upload": ("upload", request.files.getlist("uploadInput")[0].read(), "application/octet-stream")})

        return redirect(f"/viewer?viewingSessionId={viewing_session_id}")
