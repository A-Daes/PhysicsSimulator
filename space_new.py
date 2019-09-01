from graphics import *
import time

class Particle:
    position = (0,0)
    name = "P"
    graphical_rep = Point(0,0)
    x_speed = 0
    y_speed = 0
    x_accel = 0
    y_accel = 0
    pot_energy = 0
    kin_energy = 0
    mass = 1
    charge = 0
    ##Construct Particle with position and name. Default is (0,0) and P
    def __init__(self, x_pos, y_pos, name):
        self.position=(x_pos,y_pos)
        self.name=name
        self.graphical_rep=Point(x_pos,y_pos)
    ##Return and set Positions
    def get_position(self):
        return self.position
    def set_position(self, new_x,new_y):
        self.position=(new_x,new_y)
        self.graphical_rep=Point(new_x,new_y)
    #return and set graphical position
    def get_graphrep(self):
        return self.graphical_rep 
    def set_graphrep(self, new_x, new_y):
        self.graphical_rep = Point(new_x, new_y)
        self.position=(new_x,new_y)
    ##Return and set Names
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name=new_name
    ##update particle based on speed
    def update_position(self): ## 0.025 for 40Hz refresh speed
        self.update_speed()
        self.x_speed = (self.x_speed + 0.025*self.x_accel)
        self.y_speed = (self.y_speed + 0.025*self.y_accel)
        self.move(self.x_speed*0.025,self.y_speed*0.025)
    def move(self,dx,dy):
        self.get_graphrep().move(dx,dy)
    def update_speed():
        ## Encontrar potencial electrico con la integral de linea
        ## Encontrar velocidad debido al potencial usando conservacion de la energia
        ## Encontrar vectores de velocidad usando los angulos (opcional?)
        pass
    


##Function to refresh view for a time period
def refreshParticles(particles,deltat):
    for step in range(deltat*40): ## 40Hz refresh speed
        for particle in particles:
            particle.update_position()
        time.sleep(0.025) ##40Hz refresh speed
        

View = GraphWin(title="View")

##Create the world
World = []

##Create a Particle
TestParticle = Particle(0,0,"Charged Particle")

##Add particle to world
World.append(TestParticle)

##Draw the world
for particle in World:
    particle.get_graphrep().draw(View)

#Update the world for 10 seconds

refreshParticles(World, 10)

for particle in World:
    print(particle.get_graphrep())





