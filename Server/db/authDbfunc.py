from Server.middleware.hash import passwordCheck,hashPassword


class SignupModel:
    def __init__(self,email,user_name,password):
        self.email=email
        self.user_name=user_name
        self.password=password
        
        
def signUp(email,user_name,password,db)-> bool:
    try:
        user=db.find_one({'email':email})
        if user:
            return False
        password=hashPassword(password)
        db.insert_one(vars(SignupModel(user_name=user_name,email=email,password=password)))
        return True
    except:
        print('An exception occurred in SignUp')
        return False
      
    
    
def login(email,password,db)-> bool:
    try:
        user=db.find_one({'email':email})
        if (not user ) or not(passwordCheck(password,user['password'])):
            return False
        return True
    except:
      print('An exception occurred login')
      return False
    
      
    