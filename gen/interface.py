from flask import Flask,  jsonify, request, send_file
from auth import requires_auth

app = Flask('first_app')

@app.route("/my-first-api/echo", methods=["GET", "POST"])

@app.route("/dobryplan", methods=["GET", "POST"])
@requires_auth
def echo():
    return request.get_data()

app.run(debug=True, port=8000)