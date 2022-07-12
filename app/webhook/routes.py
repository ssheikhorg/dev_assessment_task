from flask import Blueprint, json, request

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    # github webhook
    data = request.get_json()
    return {"Hello": "world"}, 200


@webhook.route('/', methods=["GET"])
def index():
    return json.dumps({"Hello": "world"}), 200
