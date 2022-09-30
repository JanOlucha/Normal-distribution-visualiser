
w = 700
class obstacle():
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    def show(self):
        fill(255,0,0)
        ellipse(self.__x,self.__y,10,10)
    def getPos(self):
        return [self.__x,self.__y]
class blob():
    def __init__(self):
        self.__x = w/2
        self.__y = 0 
        self.__xVel = 0
        self.__yVel = 0 
        self.__xAcc = 0
        self.__yAcc = 0.2
        self.__radius  = 5
        self.__stoped = False
        self.__accounted = False
    def checkCollision(self):
            global obstacles
            for i in obstacles:
                if abs(self.__x-i.getPos()[0])<=10 and abs(self.__y-i.getPos()[1])<=10:
                    return True
    def update(self):
        global bins
        if not self.__stoped:
            if self.checkCollision():
                #update velocities
                newVelX = random(-2,2)
                newVelY = -2
                self.__xVel += newVelX
                self.__yVel += newVelY
            self.__xVel += self.__xAcc
            self.__yVel += self.__yAcc
            self.__x += self.__xVel
            self.__y += self.__yVel
            if self.__y >= w or self.__stoped == True:
                self.__stoped = True
                self.__yAcc=0
                self.__yVel=0
                self.__y=w-self.__radius
                self.__xAcc = 0
                self.__xVel = 0
            self.__xVel*=0.99
            self.__yVel*=0.99
        else:
            #find in which bin it fits
            if not self.__accounted:
                for x in range(bins-1):
                    if self.__x > x*(w/bins) and self.__x < (x+1)*(w/bins):
                        bin[x] += 1
                self.__accounted = True
                self.reset()
    def show(self):
        fill(0,255,0)
        ellipse(self.__x,self.__y,self.__radius,self.__radius)
    def reset(self):
        self.__x = w/2
        self.__y = 0 
        self.__xVel = 0
        self.__yVel = 0 
        self.__xAcc = 0
        self.__yAcc = 0.2
        self.__radius  = 5
        self.__stoped = False
        self.__accounted = False
n = 7
blobCount = 4
b = blob()
h = w - 100
bins = 15
bin = [0 for i in range(bins)]
blobs = [blob() for i in range(blobCount)]
obstacles = []
for i in range(n):
    for j in range(n):
        obstacles.append(obstacle(h*i/n+(h/n),h*j/n+(h/n)))
def drawColumns():
    for x in range(bins-1):
        fill(0,0,255)
        rect(x*(w/bins),w,w/bins,-bin[x]*20)
        
def setup():
    size(w,w)
    background(0)

def draw():
    background(0)
    for i in blobs:
        i.update()
        i.show()

    for i in obstacles:
        i.show()
    print(bin)
    drawColumns()
   
        
        
