let center;
let pi;
// initiating the center and pi variables 

const circleRaius = 200;
// radius of the circle 

let circlePoints = [];
// collection of points that the circle pass through 

let circumference = 0;
// circumference of the circle 

let slider;
// slider object for contorlling the number of triangles inside the circle 


function setup() {
  createCanvas(700, 575);
  // creating the canvas 

  center = [width / 2, height / 2];
  slider = createSlider(3, 500, 30, 1);
  slider.style("width", `${width}px`);
  // initiating the coordinates of center of the circle and slider 

  slider.input(drawTriangles);
  // adding an event listener function 

  angleMode(DEGREES);
  // setting the angle mode to degrees 

  noLoop();
  // disabling continous rendering to save energy
}

function drawTriangles() {
  background(0);
  // resetting the background

  circlePoints = [];
  circumference = 0;
  pi = 0
  // resetting the collection of points that the circle pass through  

  const noOfTriangles = slider.value();
  // getting the number of triangles to render 

  circle(center[0], center[1], circleRaius * 2);
  // rendering a circle to show the actual circle in the background 


  beginShape();
  // starting the shape 

  fill(123, 54, 34);
  stroke(255, 0, 255);
  strokeWeight(3);


  for (let i = 0; i <= 360; i += (360 / noOfTriangles)) {
    const x = center[0] + cos(i) * circleRaius;
    const y = center[1] + sin(i) * circleRaius;
    // getting the coordinates of the points of triangle 

    circlePoints.push([x, y]);
    // adding the point to the collection of points 
  }

  vertex(circlePoints[0][0], circlePoints[0][1]);
  for (let index = 1; index < circlePoints.length; index++) {
    const point = circlePoints[index];
    const previousPoint = circlePoints[index - 1];
    // getting the current and previous points    

    circumference += dist(previousPoint[0], previousPoint[1], point[0], point[1]);
    // calculating the circumference 
    vertex(point[0], point[1])
  }

  endShape();

  /* 
  circumference = 2* PI * RADIUS
  Dividing both side by 2 * RADIUS we get,
  PI = circumference / (2 * RADIUS)
  */

  fill(255, 255, 255);
  stroke(0, 0, 0);
  strokeWeight(1);
  // resetting the stroke

  pi = circumference / (2 * circleRaius);
  // calculating pi 

  text(`PI approximation: ${pi}`, width - 230, 10);
  // rendering the value of pi to screen 

  redraw();
  // redrawing the circle 

}

function draw() {
  drawTriangles(50);
  // drawing the triangles 
}
