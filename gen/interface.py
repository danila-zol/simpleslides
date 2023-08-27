from flask import Flask,  jsonify, request, send_file, render_template
from flask_cors import CORS
from auth import requires_auth, validator
from pptx import Presentation
from processing import get_md
import json
import uuid



app = Flask('first_app')
CORS(app)

@app.route("/echo", methods=["GET", "POST"])
@requires_auth
def echo():
     return request.get_data()

@app.route("/dobryplan", methods=["GET", "POST"])
@requires_auth
def serve():
    if (request.method == 'POST'):
        validator.user_init(request.get_json())
        return generate_user_json(request.get_json())
        # return { 
        #         'mtype' : 'success',
        #         'result' : [
        #              {
        #                   'type' : 'pdf',
        #                   'link' : '$SOME_LINK.pdf'
        #              },
        #              {
        #                   'type' : 'json',
        #                   'link' : '$SOME_LINK.json'
        #              }
        #         ]
        #     }
    else:
        return render_template('404.html'), 404

@app.route("/dobryplan/<file_dest>")
#@requires_auth
def serve_docs(file_dest):
    return send_file(f"gen/user_content/{file_dest}")

class generated_deck :
        def __init__(self):
            self.formats = []
            self.pdf
        def generate(user_data):
            pass

def generate_user_json(user_init):
    response = {
        'mtype' : 'ginfo',
        'status' : 'success',
        'result' : {}
    }

    md_presentation = get_md(user_init['user_info'])

    #basename = f"{ user_init['userid'] }{ uuid.uuid4().hex }.pptx"
    #fpath = f"gen/user_content/{basename}"

    #response['result']['type'] = 'pptx'
    #response['result']['link'] = f"/dobryplan/{basename}"

    print(str(f"OpenAI object recieved"))
    print(md_presentation)
    with open("test_presentation.md", "w") as f:
         f.write(md_presentation)

    return response

    # When we add new fancy functions
    #################################
    # result_field = response.result
    # formats = generated_deck.formats.keys()
    # for f in formats:
    #     result_field.append['type'] = f
    #     result_field.link = server_store(generated_deck['f'], userid)

#def server_store(deck, userid):    



app.run(debug=True, port=5000, host='0.0.0.0')