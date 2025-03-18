class Pkt:
    def __init__(self,x: int,y: int):
        self._x = x
        self._y = y
        
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,a):
        if a <0:
            raise ValueError("x has to be grater than 0")
        self._x = a    
    
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,a):
        if a <0:
            raise ValueError("y has to be grater than 0")
        self._y = a
    
    def print_pkt(self):
        print(f"(x: {self._x} y: {self._y})")
        
    @staticmethod
    def Fib(n: int):
        x = [1,1]
        print(x[0])
        print(x[1])
        for _ in range(2,n):
            xp = x[1]
            x[1] = x[0] + x[1]
            x[0] = xp    
            print(x[1])
        
if __name__ == '__main__':
    pkt1 = Pkt(6,4)
    pkt1.x = 10 
    print(pkt1.x)
    
            
        
        
