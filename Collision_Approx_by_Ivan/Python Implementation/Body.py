from typing import Self

class Body:
    def __init__(self, mass:float, side:float, position:float, velocity:float) -> None:
        """
        Handles all the logic for a body for calculating PI
        """        
        self.mass = mass
        self.side = side
        self.position = position
        self.velocity = velocity
        # initializing the parameters 

    def update(self, deltaTime:float) -> None:
        """updating position and handling wall collision"""
        self.position += self.velocity * deltaTime
        self.collideWallHandle()

    @property
    def right(self):
        return self.position + self.side

    def isColliding(self, other:Self) -> bool:
         """
         checks if the body is colliding with any other body
         """ 
         return other.position+other.side > self.position and self.position+self.side > other.position

    def isCollidingWall(self) -> bool:
        """
        chekcing if the body is colliding with the wall
        """ 
        return self.position <= 0

    def collideWallHandle(self) -> None:
        """
        Negating the velocity if the body is colliding with wall 
        """
        
        self.velocity *= -1 if self.isCollidingWall() else 1

    def collisionHandle(self, other:Self) -> None:
        """
        Handles collision with the other body
        """
        
        if self.isColliding(other):
            velocity = (((self.velocity*(self.mass-other.mass)) + (2*other.mass*other.velocity)) / (self.mass + other.mass))
            # velocity equation is taken from the README.md file in the root directory
            
            otherVelocity = (((other.velocity*(other.mass-self.mass)) + (2*self.mass*self.velocity)) / (other.mass + self.mass))
            # velocity equation is taken from the README.md file in the root directory

            self.velocity = velocity
            other.velocity = otherVelocity
            # updating velocity   