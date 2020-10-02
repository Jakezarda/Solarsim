import numpy as np
from rungekutta import rk4

class particle:
    mass = 0.0
    pos = np.zeros(3)
    vel = np.zeros(3)
    
    def __init__(self, mass, pos_0, vel_0):
        self.mass = mass
        self.pos = pos_0
        self.vel = vel_0      ## put check on these to make sure you have 3 values
        
        
    def update(self, t, h, f):
        y = np.zeros(6)
        for i in range(0,3):
            y[2*i] = self.pos[i]
            y[2*i+1] = self.vel[i]
        y = rk4(t, y, h, f)
        for i in range(0,3):
            self.pos[i] = y[2*i]
            self.vel[i] = y[2*i + 1]
            
            
class planet(particle):
    a = 0.0
    e = 0.0
    elong = 0.0
    r_ep = 0.0
    r_ps = 0.0
    
    
    def __init__(self, mass, pos_0, vel_0, a, e):
        self.mass = mass
        self.pos_0 = pos_0
        self.vel_0 = vel_0
        self.a = a
        self.e = e
        
   # def visviva():          ## didn't give me variables
        
        
        
