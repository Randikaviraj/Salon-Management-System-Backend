from Server.db import  db


# get reference to Dahboard collection
dashboard=db['Dashboard']

class Dashboard:
    def __init__(self,email,name) -> None:
        self.email=email
        self.name=name
        self.day_one={}
        self.day_two={}
        self.day_three={}
        self.day_four={}
        
        

def addDashBoard(email,name):
    try:
        dashboard.insert_one(vars(Dashboard(email,name)))
    except:
        print('An exception occurred addDashBoard')
        raise Exception("An exception occurred addDashBoard")
    
def deleteDashBoard(email,name):
    try:
        dashboard.delete_one({"email":email,"name":name}) 
    except:
      print('An exception occurred deleteDashBoard')