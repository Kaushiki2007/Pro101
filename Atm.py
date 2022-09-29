class atm(object) :
    """
     Blue print for atm
    """
     def __init__(self,model,color,company,speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelarating...")
        "accelarator functionality here"
        
    def change_gear(self,gear_type):
        print("gear changed")
        "gear related functionality here"

    audi = Car("A6","black","audi",80)
    print(audi.start())
