from Body import Body
# importing all the module 

# DISCLAIMER 
# This is optimized for larger number of digits, there will be error when trying digits lesser than 6 

def calculateDeltaTime(body1:Body, body2:Body, totalDigits:int) -> float:
    """
    Calculates Delta Time based on the number distance between the objects for fastening up the process
    """
    x = body1.position - body2.right
    if x > 50:
        return 1.0
    elif x > 30:
        return 1e-1
    elif x > 1.2:
        return 1e-2
    elif x > 0.5:
        return 1e-4
    elif x > 0.1:
        return 1e-6
    return 10**(-totalDigits)

def updateValue(body1:Body, body2:Body, piDigits) -> None:
    """
    Adds 1 to the value of piDigits whenver the 
    """
    if body2.isCollidingWall() or body2.isColliding(body1):
        piDigits += 1
        print(f"[PI] {piDigits}", end='\r')
    return piDigits

def simulateFrame(body1:Body, body2:Body, deltaTime:float, piDigits:int):
    """
    Simulates a Frame for calculating the value of PI
    """
    body1.collisionHandle(body2)
    # handling the collision between bodies

    piDigits = updateValue(body1, body2, piDigits)
    # updating the value of pi

    body1.update(deltaTime)
    body2.update(deltaTime)
    # updating both the bodies

    return piDigits
    

def shouldKeepSimulating(body1:Body, body2:Body) -> bool:
    """
    Returns True if the digits are calculated
    """
    return not ( ( (body1.velocity > 0) and (body2.velocity > 0) and (body1.velocity > body2.velocity) ) or (body2.velocity == body1.velocity) )

def simulate(body1:Body, body2:Body, totalDigits:int) -> int:
    """
    Simulates Physics to calculate the value of PI
    """
    piDigits = 0
    # digits of pi

    print("Simulation started.")
    totalIteration = 0
    while shouldKeepSimulating(body1, body2):
        deltaTime = calculateDeltaTime(body1, body2, totalDigits)
        piDigits = simulateFrame(body1, body2, deltaTime, piDigits)
        # simulates bodies

        totalIteration +=1

    print(f"[Iterations] {totalIteration}")

    return piDigits


if __name__ == "__main__":

    totalDigits = 4
    # the number of digits to be calculated by the program

    body1 = Body(100**(totalDigits-1), 100, 300, -2)
    body2 = Body(1, 30, 30, 0)
    # initializing the bodies
    
    print("Final value", simulate(body1, body2, totalDigits))
    # simulating the program 