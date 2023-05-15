class Body{
    constructor(mass, side, position, velocity){
        this.mass = mass;
        this.side = side;
        this.position = position;
        this.velocity = velocity;
        // initializing the parameters 
    }

    update(){
        this.position += this.velocity;
        this.collideWallHandle();
        // updating position and handling wall collision 
    }

    isColliding(other){
        return other.position+other.side > this.position && this.position+this.side > other.position;
        // checks if the body is colliding with any other body 
    }

    isCollidingWall(){
        return this.position <= 0;
        // chekcing if the body is colliding with the wall 
    }

    collideWallHandle(){
        if (this.isCollidingWall()) {
            this.velocity *= -1;
            // this negates the velocity 
        }
        // handling collision with the wall
    }

    collisionHandle(other){
        if(this.isColliding(other)){
            const velocity = (((this.velocity*(this.mass-other.mass)) + (2*other.mass*other.velocity)) / (this.mass + other.mass))
            // velocity equation is taken from the README.md file in the root directory
            
            const otherVelocity = (((other.velocity*(other.mass-this.mass)) + (2*this.mass*this.velocity)) / (other.mass + this.mass))
            // velocity equation is taken from the README.md file in the root directory

            this.velocity = velocity;
            other.velocity = otherVelocity;
            // updating velocity 
        }
        // handling the collision 
    }

    render(){
        square(this.position, height-this.side, this.side);
        // rendering the square 
    }
}