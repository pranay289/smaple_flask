from flask import Flask
from flask import redirect
from flask import request,url_for,jsonify
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def return_pages():
    if request.method == 'GET':
        # details = request.json
        # email = details["email"]
        return jsonify({"email":"sucess"})

# @app.route('/second_page')
# def second_page():
#     if request.method == 'GET':
#         return {"page":"Second","username":"pranay"}

app.run()


