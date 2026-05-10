from flask import Flask,request,url_for,redirect,jsonify
import os

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def h():
    if(request.method =="POST"):
        data=request.get_json()
        json={"you_send":data.get("name","BHAVISHYA")}
        return jsonify(json)
    else:
        return "TRUE"


if __name__ == "__main__":
    aprt=int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=aprt)
    
