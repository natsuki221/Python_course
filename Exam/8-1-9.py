class Leg():
    
    def __init__(self, num, look):
        
        self.num = num
        self.look = look
    
class Animal():
    
    def __init__(self, name, leg):
        
        self.__name = name
        self.leg = leg
    
    def show_name(self):
        return self.__name
    def show(self):
        print(self.show_name(), '有', self.leg.num, '隻', self.leg.look, '腿', sep='')

leg = Leg(4, 'shorty')

ani = Animal('Dog', leg)

ani.show()