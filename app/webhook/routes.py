from flask import Blueprint, json, request
from ..extensions import insert_extension
from datetime import datetime


webhook = Blueprint("Webhook", __name__, url_prefix="/webhook")


@webhook.route("/receiver", methods=["POST"])
def receiver():
    if request.headers["Content-Type"] == "application/json":
        event = request.json
        print(event)
        if request.headers["X-GitHub-Event"] == "push":
            data = {
                "request_id": event["sender"]["id"],
                "author": event["pusher"]["name"],
                "action": event["pusher"]["name"] + " pushed to " + event["repository"]["name"],
                "from_branch": event["repository"]["name"],
                "to_branch": event["repository"]["full_name"],
                "timestamp": datetime.timestamp(datetime.now()),
            }
        elif request.headers["X-GitHub-Event"] == "pull_request":
            data = {
                "request_id": event["sender"]["id"],
                "author": event["pull_request"]["user"]["login"],
                "action": event["pusher"]["name"] + " pushed to " + event["repository"]["name"],
                "from_branch": event["pull_request"]["head"]["ref"],
                "to_branch": event["pull_request"]["base"]["ref"],
                "timestamp": datetime.timestamp(datetime.now()),
            }
        insert_extension(data)
        return json.dumps({"status": "success"})

    return json.dumps({"status": "error"})


@webhook.route("/", methods=["GET"])
def index():
    return json.dumps({"Hello": "world"}), 200
