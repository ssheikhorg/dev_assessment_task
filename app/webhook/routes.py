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
                "request_id": event["request_id"],
                "author": event["sender"]["login"],
                "action": event["action"],
                "from_branch": event["repository"]["name"],
                "to_branch": event["repository"]["full_name"],
                "timestamp": datetime.timestamp(datetime.now()),
            }


@webhook.route("/", methods=["GET"])
def index():
    return json.dumps({"Hello": "world"}), 200
