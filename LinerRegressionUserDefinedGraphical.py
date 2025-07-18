import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    #Load the Data
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]

    print("Values of Independent variables : ",X)
    print("Values of Dependent variables : ",Y)

    mean_x=np.mean(X)
    mean_y=np.mean(Y)

    print("X_MEAN is : ",mean_x)
    print("Y_MEAN is : ",mean_y)

    n=len(X)

    numerator = 0
    denomenator = 0

    #y=mx+c
    for i in range(n):
        numerator=numerator+(X[i]-mean_x)*(Y[i]-mean_y)
        denomenator=denomenator+(X[i]-mean_x)**2

    m=numerator/denomenator
    print("Slope of line  : ",m)

    C=mean_y-(m*mean_x)
    print("Y intercept of line is : ",C)

    x=np.linspace(1,6,n)
    y = C + m * x
    plt.plot(x,y,color='orange',label='Regression Line')
    plt.scatter(X,Y,color='green',label='Scatter Plot')
    plt.xlabel("X:Independent Variables")
    plt.ylabel("Y:Dependent Variables")

    plt.legend()
    plt.show()
    

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()