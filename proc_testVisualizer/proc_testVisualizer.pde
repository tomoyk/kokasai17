import processing.sound.*;
import processing.serial.*;

/* Viewer */
boolean status = false; // Now status
boolean before = true; // Before status
PImage closeImg, openImg;
SoundFile hi, bye;

/* Srial */
Serial port;
float val;

void settings(){
  size(1300, 700);
}

void setup(){
  /* Serial */
  frameRate(60);
  String arduinoPort = Serial.list()[0];
  port = new Serial(this, arduinoPort,9600);
  
  /* Image and Sounds */
  noStroke();
  setBack();
  closeImg = loadImage("/home/tkoyama/kokasai17/proc_testVisualizer/door_close.png");
  openImg = loadImage("/home/tkoyama/kokasai17/proc_testVisualizer/door_open.png");
  hi = new SoundFile(this, "/home/tkoyama/kokasai17/proc_testVisualizer/door_hello.wav");
  bye = new SoundFile(this, "/home/tkoyama/kokasai17/proc_testVisualizer/door_close.wav");
}

void setBack(){
  background(#cccccc);
}

void draw(){
  if(port.available() > 0){
    val = port.read();
    println("test: "+val);
    
    if( val == 1.0 ){
      status = true;
    }else{
      status = false;
    }
    
    if(status && !before){ // open
      before=true;
      setBack();
      image(closeImg, 200, 0);
      bye.play();      
    }else if(!status && before){ // close
      before=false;
      setBack();
      image(openImg, 200, 0);
      hi.play();
    }
    
  }
  
  stroke(120);
  fill(255);
}
