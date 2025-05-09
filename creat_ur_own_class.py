# boiler plate
class ClassName:   # Pascal case
    def __init__(self , value2): # two ways of declaring attributes
        self.class_atr1 = 1 # is inbuilt 
        self.class_atr2 = value2 # defining attributes, will take attribute when the object is being created
    
    # defining methods
    def method_name(self):  
        self.class_atr = 2   # affecting the attributes, it is similar to a function which an object can do


# another way of declaring attribute if we are not defining it in the constructor, example below
# class ClassName:
#    pass
# 
# user1 = ClassName()\
# user1.atr1 = "value1"
# user1.atr2 = "value2"