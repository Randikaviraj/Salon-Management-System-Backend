from functools import wraps
from flask import Response,request,g

from Server.middleware.token import decode_auth_token,encode_auth_token


def authMiddleware(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:
            token=request.headers['Authorization']
            email=decode_auth_token(token)
            g.email=email
            g.token=encode_auth_token(email)
            return func(*args,**kwargs)
        except:
          return Response('Auth Failed',mimetype='text/plain',status=401)
        
    return wrapper