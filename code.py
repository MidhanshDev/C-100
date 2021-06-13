class Car(object):
    def __init__(self,modal,color,company,speedlimit):
       self.color=color
       self.modal= modal
       self.company= company
       self.speedlimit = speedlimit
    
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("Accelerating")
    def changegear(self,geartype):
        print("gear changed ", geartype)
audi = Car("A6","white","audi","160") 
print (audi.color)
audi.changegear(3)
