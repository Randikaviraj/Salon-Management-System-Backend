from Server.db import db
from Server.db.authDbfunc import signUp,login


# get reference to Seller collection
sellerdb=db['Seller']


def sellerLogin(email,password)->bool:
  return login(email,password,sellerdb)

def sellerSignUp(email,user_name,password)-> bool:
  return signUp(email,user_name,password,sellerdb)