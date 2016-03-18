from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/sum/<a>/<b>',methods= ['GET'])
def sum(a,b):
    result = int(a) + int(b)
    return jsonify({'result':result})

app.run(debug=True)
