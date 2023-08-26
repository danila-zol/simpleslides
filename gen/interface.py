from flask import Flask,  jsonify, request, send_file, render_template
from auth import requires_auth, validator
import json

app = Flask('first_app')

@app.route("/my-first-api/echo", methods=["GET", "POST"])
@requires_auth
def echo():
     return request.get_data()

@app.route("/dobryplan", methods=["GET", "POST"])
@requires_auth
def serve():
    if (request.method == 'POST'):
        #return generate_user_json(request.get_json()['userid'])
        validator.user_init(request.get_json())
        return { 
                'mtype' : 'success',
                'result' : [
                     {
                          'type' : 'pdf',
                          'link' : '$SOME_LINK.pdf'
                     },
                     {
                          'type' : 'json',
                          'link' : '$SOME_LINK.json'
                     }
                ]
            }
    else:
        return render_template('404.html'), 404
    
class generated_deck :
        def __init__(self):
            self.formats = []
            self.pdf
        def generate(user_data):
            pass

def generate_user_json(userid):
    response = {
        'mtype' : 'ginfo',
        'status' : 'success',
        'result' : []
    }

    result_field = response.result
    formats = generated_deck.formats.keys()
    for f in formats:
        result_field.append['type'] = f
        result_field.link = server_store(generated_deck['f'], userid)

#def server_store(deck, userid):    


app.run(debug=True, port=8000, host='0.0.0.0')