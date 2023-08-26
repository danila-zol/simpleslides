from flask import Flask,  jsonify, request, send_file, render_template
from auth import requires_auth
import json

app = Flask('first_app')

@app.route("/my-first-api/echo", methods=["GET", "POST"])

@app.route("/dobryplan", methods=["GET", "POST"])
@requires_auth
def serve():
    if (request.method == 'POST' and
        request.get_json['mtype'] == 'initialization'):
        return generate_user_json(request.get_json()['userid'])
    else:
        return render_template('404.html'), 404

def generate_user_json(userid):
    response = {
        'mtype' : 'ginfo',
        'status' : 'success',
        'result' : {}
    }

    class generated_deck :
        def __init__(self):
            self.formats = []
            self.pdf
        def generate(user_data):
            pass

    for result_field in response.result:
        format_list = generated_deck.formats
        for f in format_list:
            


app.run(debug=True, port=8000)