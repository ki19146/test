# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:51:58 2021

@author: 小马
"""

import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
from matplotlib.pyplot import MultipleLocator
import random

#creat the graph
fig = plt.figure()
ax = fig.add_subplot()
ax=plt.gca()

PInfected_y = []
DayIn_x = []

PRecovery_y = []
DayRe_x = []

PDead_y = []
DayD_x = []

def init(): # Initialization function
    return []

Days = 1
def update(Days):
    PInfected1 = random.uniform(0.4,0.7)  # The probability of infecting before lock down
    PInfected2 = random.uniform(0.2,0.5)  # The probability of infecting after lock down
    PDead1 = random.uniform(0.07,0.09)  # The probability of death before lock down
    PDead2 = random.uniform(0.009,0.04)  # The probability of death after lock down
    PRecovery1 = random.uniform(0.4, 0.6) # The probability of recovery before lock down
    PRecovery2 = random.uniform(0.6, 0.7)  # The probability of recovery after lock down
    Infected=1500 
    Dead=100
    Recovery=350 
   
    if Days <= 40:
        Infected +=(Infected*PInfected1)
        Dead +=(Dead*PDead1)
        Recovery +=(Recovery*PRecovery1) 
    elif Days > 40:
        Infected +=(Infected*PInfected2)
        Dead +=(Dead*PDead2)
        Recovery +=(Recovery*PRecovery2)
    
    
    DayIn_x.append(Days)
    PInfected_y.append(Infected)

    DayRe_x.append(Days)
    PRecovery_y.append(Recovery)
       
    DayD_x.append(Days)
    PDead_y.append(Dead)

    plt.plot(DayIn_x,PInfected_y,c = "r")
    plt.plot(DayRe_x,PRecovery_y,c = "g")
    plt.plot(DayD_x,PDead_y,c = "b")
    
    plt.title('The spread of coronabirus in B city',fontsize=24)
    plt.xlabel('Days',fontsize=14)
    plt.ylabel('Number of People per day',fontsize=14)
    x_major_locator=MultipleLocator(5) # Set the scale interval of the x-axis to 5, and store it in the variable
    y_major_locator=MultipleLocator(100) # Set the scale interval of the y-axis to 100, and store it in the variable
    ax.xaxis.set_major_locator(x_major_locator) # Set the main scale of the x-axis to a multiple of 1
    ax.yaxis.set_major_locator(y_major_locator) # Set the main scale of the y-axis to a multiple of 10
    return [ax]

ani= FuncAnimation(fig, update, frames=range(100), init_func=init, interval=10, repeat = False) 
ani.save('lines.gif',writer = 'Tianyu Ma')  
plt.show() 