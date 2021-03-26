from Server.db import db
from Server.middleware.hash import passwordCheck,hashPassword


# get reference to Ueser collection
userdb=db['Users']

class UserLoginModel:
    def __init__(self, email, password):
      self.email = email
      self.password = password

class UserSignupModel:
    def __init__(self,email,user_name,password):
        self.email=email
        self.user_name=user_name
        self.password=password
        
        
def signUp(email,user_name,password)-> bool:
    try:
        user=userdb.find_one({'email':email})
        if user:
            return False
        password=hashPassword(password)
        userdb.insert_one(vars(UserSignupModel(user_name=user_name,email=email,password=password)))
        return True
    except:
        print('An exception occurred in SignUp')
        return False
      
    
    
def login(email,password)-> bool:
    try:
        user=userdb.find_one({'email':email})
        if (not user ) or passwordCheck(password,user['password']):
            return False
        return True
    except:
      print('An exception occurred login')
      return False
    
      
    