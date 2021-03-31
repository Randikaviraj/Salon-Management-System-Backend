import json
from flask import Blueprint,g,Response,request
from Server.middleware.auth_middleware import authMiddleware
from Server.db.userDB import userLogin,userSignUp
from Server.middleware.token import encode_auth_token


client_route=Blueprint("client_route",__name__)



@client_route.route('/login',methods=["POST"])
def login_route():
    try:
        email=request.json['email']
        password=request.json['password']

        if userLogin(email,password):
            response=Response(status=200)
            response.headers['Authorization']=encode_auth_token(email)
            return response 
        
        return Response(status=401)
    except Exception as e:
        print(e)
        return Response(status=401)
    
@client_route.route('/signup',methods=["POST"])
def signup_route():
    try:
        name=request.json['name']
        email=request.json['email']
        password=request.json['password']
        if userSignUp(email,name,password):
            return json.dumps({'email':email,'name':name}), 200
            
    except:
        print('An exception occurred signup_route')
        return Response(status=401)



@client_route.route("/home",methods=["POST"])
@authMiddleware
def home():
    # g.email
    response=Response()
    response.headers['Authorization']=g.token
    response.status=200
    return response
    

