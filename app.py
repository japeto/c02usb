import random as rd

from flask import Flask
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
	return {"message": "hello"}

@app.route("/random", methods=['GET'])
def random():
	return {"guess": rd.randint(3, 20)}

app.run(host="0.0.0.0", debug=True, port=8025)
