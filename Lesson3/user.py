class User:
    def __init__(self,first_name,last_name):
      self.first_name=first_name
      self.last_name=last_name
      
    def sayName(self):
        print(self.first_name)
        
    def sayLastName(self):
         print(self.last_name)
     
    def sayFullName(self):
         print(self.first_name,self.last_name)
         
    