import processing.serial.*;

Serial port;
float val;

void setup(){
  size(600,600);
  frameRate(60);
  String arduinoPort = Serial.list()[1];
  port = new Serial(this, arduinoPort,9600);
  background(255);
}

void draw(){
  if(port.available() > 0){
    val = port.read();
    println("test: "+val);
    
    if(val==1.0){ //close
      fill(0, 0, 120);
      ellipse(300, 300, width/2, height/2);
    }else{ //open
      fill(0, 255, 0);
      ellipse(300, 300, width/2, height/2);
    }
  }
  
  stroke(120);
  fill(255);
}