from distutils.command.sdist import sdist
from math import sin
import matplotlib.pyplot as plot

class Bisection:
    def __init__(self,value1,value2,precision):
        self.x0=value1
        self.x1=value2
        self.precise=precision
        self.arr=[]
        self.arr1=[]

    def display(self):
        print("{}           |   {}      |   {}      |   {}      |   {}".format(self.count,round(self.x0,3),round(self.x1,3),round(self.xn,3),round(self.equation,3)))

    def calculate(self):
        if(self.x1*self.x0<0):
            print("iteration   |   xo       |   x1      |   xn      |   f(xn)")
            self.xn=(self.x0+self.x1)/2
            self.equation=sin(self.xn)-pow(self.xn,2)-self.xn+3
            self.count=1
            self.display()
            self.arr.append(round(self.xn,3))
            self.arr1.append(round(self.equation,3))
            while(abs(self.x1-self.x0)>self.precise):
                self.xn=(self.x0+self.x1)/2
                self.equation=sin(self.xn)-pow(self.xn,2)-self.xn+3
                if(self.equation<0):
                    self.x1=self.xn
                else:
                    self.x0=self.xn
                self.arr.append(round(self.xn,3))
                self.arr1.append(round(self.equation,3))
                self.count+=1
                self.display()
            print("The root of the given equation is :",round(self.xn,3))
        else:
            print("Wrong initital value ")

    def graph(self):
        srt1=sorted(self.arr)[-1]
        plot.plot(self.arr,'bo',self.arr1,'k')
        plot.text(0,srt1,'xn')
        plot.text(0,0,'f(x)')
        plot.title('dot represents value of xn at each interval and line represents value of f(xn) at each interval')
        plot.grid(True)
        plot.show()
        


        
xo,x1=input("Enter the two roots").split(' ')
prec=float(input("Enter the precison of the value "))
bisec=Bisection(float(xo),float(x1),prec)
bisec.calculate()
if(float(x1)*float(xo)<0):
    choice=input("Do want to see the graph")
    choices=['yes','y','graph','see']
    if(choice in choices):
        bisec.graph()

            

