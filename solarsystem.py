import numpy as np
import particles as particle    ##I don't want to go and remove the s from all of those below
import xlrd
import matplotlib.pyplot as plt


databook = xlrd.open_workbook('planetdata3.xlsx')
datasheet = databook.sheet_by_name('planetdata3')


m = datasheet.row_values(5)
pos_x = datasheet.row_values(0)
pos_y = datasheet.row_values(1)
vel_x = datasheet.row_values(3)
vel_y = datasheet.row_values(4)

##initial conditions 
pos_me = np.array([pos_x[0], pos_y[0], 0.0])
pos_v = np.array([pos_x[1], pos_y[1], 0.0])
pos_e = np.array([pos_x[2], pos_y[2], 0.0])
pos_m = np.array([pos_x[3], pos_y[3], 0.0])
pos_j = np.array([pos_x[4], pos_y[4], 0.0])
pos_s = np.array([pos_x[5], pos_y[5], 0.0])
pos_u = np.array([pos_x[6], pos_y[6], 0.0])
pos_n = np.array([pos_x[7], pos_y[7], 0.0])

vel_me = np.array([vel_x[0], vel_y[0], 0.0])
vel_v = np.array([vel_x[1], vel_y[1], 0.0])
vel_e = np.array([vel_x[2], vel_y[2], 0.0])
vel_m = np.array([vel_x[3], vel_y[3], 0.0])
vel_j = np.array([vel_x[4], vel_y[4], 0.0])
vel_s = np.array([vel_x[5], vel_y[5], 0.0])
vel_u = np.array([vel_x[6], vel_y[6], 0.0])
vel_n = np.array([vel_x[7], vel_y[7], 0.0])

Mercury = particle.particle(m[0], pos_me, vel_me)      
Venus = particle.particle(m[1], pos_v, vel_v)
Earth = particle.particle(m[2], pos_e, vel_e)
Mars = particle.particle(m[3], pos_m, vel_v)
Jupiter = particle.particle(m[4], pos_j, vel_j)
Saturn = particle.particle(m[5], pos_s, vel_s)
Uranus = particle.particle(m[6], pos_u, vel_u)
Neptune = particle.particle(m[7], pos_n, vel_n)
planets = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]


G = 39.2196
M_sun = 333000
def f(t,y):
    pos = np.array([y[0], y[2], y[4]])
    acc = np.zeros(3)
    r_mag = np.sqrt(y[0]*y[0] + y[2]*y[2] + y[4]*y[4])
    r_hat = -pos/r_mag
    acc += (G*M_sun/(r_mag*r_mag))*r_hat
    for planet in planets:                                                            ##general process should be what we did for sun 
        r_pp = planet.pos - pos                                                       ## "R_12 planet.pos - pos
        r_mag = np.sqrt(r_pp[0]*r_pp[0] + r_pp[1]*r_pp[1] + r_pp[2]*r_pp[2])          ## passing y array for any planet to this
        if (r_mag > 0.1):                                                             ## "for planet in planets"
            r_hat = r_pp/r_mag                                              
            acc += ((G*planet.mass)/(r_mag*r_mag))*r_hat
    f = np.array([y[1], acc[0], y[3], acc[1], y[5], acc[2]])
    return f
    
h = 0.05
N = 3250

print(pos_x[0])
out_file = open('solarsystem.dat' , 'w')
for i in range(0, N):
    t = h + i*h
    for p in planets:
        p.update(t,h,f)
    '''out_file.write(str(t) + " " + str(planets[0].pos[0]) + " " + str(planets[0].pos[1]) + " " + str(planets[0].vel[0]) + " " + str(planets[0].vel[1]) + " " + str(planets[1].pos[0]) + " " + str(planets[1].pos[1]) + " " + str(planets[1].vel[0]) + " " + str(planets[1].vel[1]) + " " + str(planets[2].pos[0]) + " " + str(planets[2].pos[1]) + " " + str(planets[2].vel[0]) + " " + str(planets[2].vel[1]) + " " + str(planets[3].pos[0]) + " " + str(planets[3].pos[1]) + " " + str(planets[3].vel[0]) + " " + str(planets[3].vel[1]) + " " + str(planets[4].pos[0]) + " " + str(planets[4].pos[1]) + " " + str(planets[4].vel[0]) + " " + str(planets[4].vel[1]) + " " + str(planets[5].pos[0]) + " " + str(planets[5].pos[1]) + " " + str(planets[5].vel[0]) + " " + str(planets[5].vel[1]) + " " + str(planets[6].pos[0]) + " " + str(planets[6].pos[1]) + " " + str(planets[6].vel[0]) + " " + str(planets[6].vel[1]) + " " + str(planets[7].pos[0]) + " " + str(planets[7].pos[1]) + " " + str(planets[7].vel[0]) + " " + str(planets[7].vel[1]) + "\n")'''
#    print(planets[0].pos[0])
    solarsimplot = plt.plot(planets[0].pos[0], planets[0].pos[1])
plt.savefig('SolarSimEarth.pdf')


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
