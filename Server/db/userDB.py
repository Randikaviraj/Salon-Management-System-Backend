from Server.db import db
from Server.db.authDbfunc import signUp,login



# get reference to Ueser collection
userdb=db['Users']

def userLogin(email,password)->bool:
 return login(email,password,userdb)

def userSignUp(email,user_name,password)-> bool:
    return signUp(email,user_name,password,userdb)
