from flask import Flask, render_template, request,jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
myapi={
    "data" : {
        "name":"uday",
        "section":"Hindustan",
        "id":36111273,
        "work":"yes"
        },
    "xhrFields" : {
        "withCredentials" : "true"
    },
    "crossDomain" : "true",
    "contentType": "application/json; charset=utf-8"
}

@app.route('/')
def login():
   return render_template('login.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      username = request.form.get("email")
      password = request.form.get("password")
      if len(username)<8:
          return "your password is too short"
      else:
          res = {"username": username,"password":password}

        
      res = {"username": username,"password":password}
      return render_template("result.html",data=res)
@app.route('/api')
@cross_origin(supports_credentials = True)
def myjson():
    return jsonify(myapi)

if __name__ == '__main__':
   app.run(debug = True)
