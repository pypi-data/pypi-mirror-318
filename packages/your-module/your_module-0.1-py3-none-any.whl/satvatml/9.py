import numpy as np
import matplotlib.pyplot as plt
def lwr(X,y,x,tau):
    weights=np.exp(-((X-x)**2)/(2*tau**2))
    weighted_sum=np.sum(weights*y)
    weights_total=np.sum(weights)
    return weighted_sum/weights_total
tau=1.0
np.random.seed(42)
X=np.linspace(1,10,100)
y=2*X+np.random.normal(0,2,X.shape)

pred=[lwr(X,y,x,tau) for x in X]
plt.figure(figsize=(8,6))
plt.scatter(X,y,label="Data points")
plt.plot(X,pred,label="LWR LINE",color="red",linewidth=2)
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.show()