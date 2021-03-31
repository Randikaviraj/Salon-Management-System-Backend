from typing import List
from pymongo import ReturnDocument
from Server.db import  db
from Server.db.dashboardDb import addDashBoard,deleteDashBoard

# get reference to Shop collection
shopdb=db['Shop']

class Shop:
    def __init__(self,email,latitude,longitude,name,services:List[dict]) -> None:
        self.email=email
        self.latitude=latitude
        self.longitude=longitude
        self.name=name
        self.services=services
        
        

def addNewShop(email,latitude,longitude,name)-> bool:
    try:
        shop=shopdb.find_one({'email':email,'name':name})
        if shop:
            return False
        addDashBoard(email,name)
        shopdb.insert_one(vars(Shop(email,latitude,longitude,name,services=[])))
        return True
    except:
        print('An exception occurred in addNewShop')
        return False
    

def deleteShop(email,name)-> bool:
    try:
        deleteDashBoard(email,name)
        shopdb.delete_one({"email":email,"name":name}) 
        return True
    except:
      print('An exception occurred deleteShop')
      return False
 
    
    
    
def changeServices(email,name,service:dict)-> bool:
    try:
        query=shopdb.find_one({'email':email,'name':name},{'_id':0, 'email':0,'name':0 ,'latitude':0,'longitude':0})
        services=query['services']
        
        for i in range(len(services)):
            if services[i]['name']==service['name']:
                services.pop(i)
                break
        services.append(service)
        
        shopdb.find_one_and_update({'email':email,'name':name},
                        { '$set': { 'services' : services} }, 
                        return_document = ReturnDocument.AFTER)
        return True
    except:
        print('An exception occurred changeServices')
        return False
    
    
    
    
def deleteService(email,name,service_name):
    try:
        query=shopdb.find_one({'email':email,'name':name},{'_id':0, 'email':0,'name':0 ,'latitude':0,'longitude':0})
        services=query['services']
    
        for i in range(len(services)):
            if services[i]['name']==service_name:
                services.pop(i)
                break
        return True
    except:
      print('An exception occurred deleteService')
      return False