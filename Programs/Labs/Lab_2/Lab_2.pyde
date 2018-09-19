


sunLocation=(250,250)
sunRadius=50
yellow=(255,255,0)

earthRadius=30
blue=(0,0,255)
earthOrbitalRadius=170
earthSpeed=0.5

marsRadius=20
red=(255,0,0)
marsOrbitalRadius=80
marsSpeed=1

moonRadius=10
white=(255,255,255)
moonOrbitalRadius=45
moonSpeed=2.3


def getLocation(orbitAroundLocation,orbitRadius,speed,time):
    centerX=orbitAroundLocation[0]+orbitRadius*sin(speed*time)
    centerY=orbitAroundLocation[1]+orbitRadius*cos(speed*time)
    return (centerX,centerY)

def drawCelestialBody(location,radius,color):
    fill(*color)
    locX,locY=location
    ellipse(locX,locY,radius*2,radius*2)    
    
class Sun:
    def __init__(self, sunLocation, sunRadius, col):
        self.Location = sunLocation
        self.Radius = sunRadius
        self.col = col
        self.p = []
    def _getLocation(self,time):
        self.Location = sunLocation
        return self.Location
    def addPlanet(self, radius, orbitalradius, col, speed):
        new_planet = Planet(self, radius, orbitalradius, col, speed)
        self.p.append(new_planet)
        return new_planet
    def draw(self, t):
        drawCelestialBody(self._getLocation(t), self.Radius, self.col)
        for i in self.p:
            i.draw(t)

class Planet(Sun):
    def __init__(self, host, Radius, OrbitalRadius, col, speed):
        self.host = host
        self.Radius = Radius
        self.col = col
        self.OrbitalRadius = OrbitalRadius
        self.speed = speed
        self.Location = getLocation(sunLocation, self.OrbitalRadius, self.speed, 0)
        self.p=[]
    def _getLocation(self, time):
        self.Location = getLocation(self.host.Location, self.OrbitalRadius, self.speed, t)
        return self.Location
        
sun=Sun(sunLocation,sunRadius,yellow)
earth=sun.addPlanet(earthRadius,earthOrbitalRadius,blue,earthSpeed)
sun.addPlanet(marsRadius,marsOrbitalRadius,red,marsSpeed)
earth.addPlanet(moonRadius,marsOrbitalRadius,white,moonSpeed)

def setup():
    global t
    global Planets
    size(500,500)
    t=0

    
def draw():
    global t
    t+=0.02
    background(0)
    sun.draw(t)