from Server.db import db

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
        
        
async def signUp(email,user_name,password)-> bool:
    try:
      await userdb.insert_one(vars(UserSignupModel(user_name=user_name,email=email,password=password)))
      return True
    except:
        print('An exception occurred in SinUp')
        return False
      
    
    
async def login(email,password)-> bool:
    try:
        user=userdb.find_one({'email':email})
        if (not user )or (user['password']!=password):
            return False
        return True
    except:
      print('An exception occurred login')
      return False
    
      
    