boolean status = false;
PImage closeImg, openImg;

void setup(){
  size(1300, 700);
  noStroke();
  closeImg = loadImage("door_close.png");
  openImg = loadImage("door_open.png");
}

void draw(){
  background(#cccccc);
  
  if(mousePressed){
    status = true;
  }else{
    status = false;
  }
  
  if(status){ // open
    image(openImg, 0, 0, 200, 200);
  }else{ // close
    image(closeImg, 0, 0, 200, 200);
  }
}