from Server.db import  db
import threading
from pymongo import ReturnDocument


# get reference to Dahboard collection
dashboard=db['Dashboard']

# global lock for threads
lock=threading.Lock()

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
      
      
def updateDashboard(day: str,hour: int,email,name,value: str,period: int): 
    # value as Not Available or availble
    try:
        dash=getDashBoard(email,name)
        with lock:
            for i in range(period):
                if len(dash[day][str(hour+period)])>0:
                    dash[day][str(hour+period)]=value
                else:
                    return None
            new=dash[day]
            return dashboard.find_one_and_update({'email':email,'name':name},
                        { '$set': { day : new} }, 
                        return_document = ReturnDocument.AFTER)               
    except:
        print('An exception occurred updateDashboard')
        raise Exception("Exption")
      
      
def getDashBoard(email,name):
    try:
      dash=dashboard.find_one({'email':email,'name':name})
      return dash
    except:
      print('An exception occurred getDashBoard')
      raise Exception("Dashboard Error")