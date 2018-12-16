import numpy as np
import win32com.client as voice
from win32com.client import Dispatch
from matplotlib import pyplot as plt
speak=voice.Dispatch("SAPI.SpVoice")
#array with each NFL team's win count, average margin of victory, strength of schedule, and a binary term dictating whether they made the playoffs or not.
data=np.array([[13,10.1,-1.2,1],[9,-3.6,-.5,1],[6,-7.0,.7,0],[5,-5.3,.3,0],[13,6.1,-1.1,1],[9,5.8,-2.4,0],[7,-3.7,-1.3,0],[0,-11.0,0.0,0],[10,9.3,-2.8,1],[9,-1.4,-2.1,1],[4,-6.1,-.3,0],[4,-8,8,-1.3,0],[10,4.8,-1.3,1],[9,5.2,-1.5,0],[6,-4.5,-.2,0],[5,-5.8,-.9,0],[13,10.1,-.7,1],[9,1.4,.2,0],[7,-2.9,1.6,0],[3,-8.9,1.3,0],[13,8.1,1.0,1],[9,2.1,0.6,0],[7,-4.0,2.1,0],[5,-3.5,2.2,0],[11,7.6,1.5,1],[11,2.1,4.3,1],[10,2.4,1.9,1],[5,-2.9,1.7,0],[11,9.3,-.2,1],[9,2.1,-.2,0],[8,-4.1,.4,0],[6,-3.3,.4,0],[14,11.9,-2.7,1],[10,-1.1,-1.3,1],[7,1.3,-1.6,1],[7,1.3,-1.6,0],[5,-8.4,-.1,0],[11,4.5,.2,1],[8,1.4,.2,0],[6,.6,.4,0],[1,-11.8,1.7,0],[9,-3.1,.4,1],[9,.2,-1.2,0],[8,1.2,-.8,0],[3,-5.1,.2,0],[12,4.9,.7,1],[12,1.9,1.3,1],[9,2.3,1.8,0],[5,-.8,.9,0],[13,7.2,-.2,1],[11,1.6,.5,1],[8,.8,1.2,0],[7,2.3,1.6,0],[10,2.8,.1,1],[9,-.8,-.6,1],[8,1.3,-.3,0],[3,-7.5,0.0,0],[11,8.4,.1,1],[7,.9,.6,0],[9,-.9,.7,0],[6,-2.1,1.1,0],[10,3.9,-1.7,1],[7,3.5,-1.9,0],[4,-10.6,-.5,0],[2,-10.7,-.5,0],[12,9.4,-2.4,1],[10,4.6,-3.0,0],[8,1.3,-1.2,0],[6,-4.9,-1.9,0],[12,8.8,1.9,1],[10,6.5,2.2,1],[5,2.6,-1.9,0],[3,-9.6,3.5,0],[9,1.6,-2.4,1]])   
#random numbers used to fill original equation
np.random.seed(0)
w1=np.random.randn()
w2=np.random.randn()
w3=np.random.randn()
b=np.random.randn()
   #equation weights and biases pre-data loop
print("BEFORE")
print(w1)
print(w2)
print(w3)
print(b)
#sigmoid function to standardize data
def sigmoid(x):
   return 1/(1+np.exp(-x))
def sigmoid_p(x):
   return sigmoid(x)*(1-sigmoid(x))
# training loop
learning_rate=.09
costs=[]
for i in range(50000):
   ri=np.random.randint(len(data))
   point=data[ri]
   
   
   z=point[0]*w1+point[1]*w2+point[2]*w3+b
   pred=sigmoid(z)
   
   target=point[3]
   cost=np.square(pred-target)
   costs.append(cost)
   
   #partial derivatives for each weight and bias
   dcost_pred=2*(pred-target)
   dpred_dz=sigmoid_p(z)
   dz_dw1=point[0]
   dz_dw2=point[1]
   dz_dw3=point[2]
   dz_db=1
   dcost_dz=dcost_pred*dpred_dz
   dcost_dw1=dcost_dz*dz_dw1
   dcost_dw2=dcost_dz*dz_dw2
   dcost_dw3=dcost_dz*dz_dw3
   dcost_db=dcost_dz*dz_db
   w1=w1-learning_rate*dcost_dw1
   w2=w2-learning_rate*dcost_dw2
   w3=w3-learning_rate*dcost_dw3
   b=b-learning_rate*dcost_db
   #from here is where the squared cost is found and then used to correct the weights and biases
if i%100==0:
   cost_sum=0
   for j in range(len(data)):
      point=data[ri]
      
      z=point[0]*w1+point[1]*w2+w3*point[2]+b
      pred=sigmoid(z)
      target=point[3]
      cost_sum+=np.square(pred-target)
      
   costs.append(cost_sum/len(data))
plt.plot(costs)
plt.show()
for i in range(len(data)):
   point=data[i]
   print(point)
   z=point[0]*w1+point[1]*w2+point[2]*w3+b
   pred=sigmoid(z)
   print("pred: {}",format(pred))
#weights and biases after the training loop
print("AFTER")
print(w1)
print(w2)
print(w3)
print(b)  
   
#computer makes is prediction
def which_team(wins,mov,sos):
   z=wins*w1+mov*w2+sos*w3+b
   pred=sigmoid(z)
   print(pred)
   if pred>.5:
      print("Playoffs")
      speak.Speak("Playoffs")
   else:
      speak.Speak("No playoffs")
      print("No Playoffs")
#2017 team data that made/didn't make the playoffs (computer was accurate w/ all 6)
print("PREDICTIONS")
which_team(13,7.2,-.2)
which_team(11,1.6,.5)
which_team(10,2.8,0.1)
which_team(3,-7.5,0)
which_team(2,-10.7,-.5)
which_team(6,-2.1,1.1)
