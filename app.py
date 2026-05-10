from flask import Flask,request,url_for,redirect,jsonify

app=Flask(__name__)
@app.route("/",methods=["POST"])
def h():
    if(request.method =="POST"):
        data=request.get_json()
        json={"you_send":data.get("name","BHAVISHYA")}
        return jsonify(json)
    else:
        return "TRUE"


        
app.run()    
